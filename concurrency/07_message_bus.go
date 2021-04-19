package concurrency

import (
	"fmt"
	"math/rand"
	"sync"
	"time"
)

/*
Source: https://levelup.gitconnected.com/lets-write-a-simple-event-bus-in-go-79b9480d8997
An Event Bus is an implementation of the pub/sub pattern where publishers are publishing data and interested subscribers
can listen to them and act based on data. This allows loose coupling of publishers from subscribers. Publishers publish
data events to the event bus, and the bus is responsible for delivering them to subscribers.

HERE we focus on topic based events. Publishers publish to topics and subscribers can listen to them.
*/

// 1. Defining data structures
// For this task, we need to define data structures to pass around.
type DataEvent struct {
	// In here we have defined underlying data to be an interface which means it can be any value. We additionally have
	// defined the topic as a member of the struct. It is possible that your subscriber could listen for more than one
	// topic. So, it is a good practice that we pass the topic so that the subscriber can distinguish between events.
	Data  interface{}
	Topic string
}

// 2. Introduce channels
// DataChannel is a channel which can accept an DataEvent
type DataChannel chan DataEvent

// DataChannelSlice is a slice of DataChannels
type DataChannelSlice []DataChannel

// 3. Event Bus
// EventBus stores the information about subscribers interested for a particular topic
type EventBus struct {
	// By using a map and defining topics, it allows us to organize events easily. A topic is treated as a key inside
	// the map. When someone publishes to it we can easily find the topic by key and then propagate the event to channels
	// for further processing.
	// We have used a mutex to protect it against concurrent access from reading and writing.
	subscribers map[string]DataChannelSlice
	rm          sync.RWMutex
}

// 3.1 Publishing to a topic
func (eb *EventBus) Publish(topic string, data interface{}) {
	// In this method, first we check if any subscriber exists for the topic. Then we just simply iterate through
	// channel slice associated with the topic and publish it.
	// NOTE that we have used a goroutine in publish method to avoid blocking the publisher.
	eb.rm.RLock()
	if chans, found := eb.subscribers[topic]; found {
		// This is done because the slices refer to same array even though they are passed by value
		// thus we are creating a new slice with our elements thus preserve locking correctly.
		channels := append(DataChannelSlice{}, chans...)
		go func(data DataEvent, dataChannelSlices DataChannelSlice) {
			for _, ch := range dataChannelSlices {
				ch <- data
			}
		}(DataEvent{Data: data, Topic: topic}, channels)
	}
	eb.rm.RUnlock()
}

// 3.2 Subscribing to a topic
func (eb *EventBus) Subscribe(topic string, ch DataChannel) {
	// Simply we are appending the subscriber to the channel slice and locking the structure and unlocking it after the
	// operation.
	eb.rm.Lock()
	if prev, found := eb.subscribers[topic]; found {
		eb.subscribers[topic] = append(prev, ch)
	} else {
		eb.subscribers[topic] = append([]DataChannel{}, ch)
	}
	eb.rm.Unlock()
}

// 4. Let’s tryout!
// First, we need to create an instance of the event bus. In a real scenario, you can export a single EventBus from the
// package making it act like a singleton.
var eb = &EventBus{
	subscribers: map[string]DataChannelSlice{},
}

func printDataEvent(ch string, data DataEvent) {
	fmt.Printf("Channel: %s; Topic: %s; DataEvent: %v\n", ch, data.Topic, data.Data)
}

func publishTo(topic string, data string) {
	for {
		eb.Publish(topic, data)
		time.Sleep(time.Duration(rand.Intn(1000)) * time.Millisecond)
	}
}

func MessageBusExample() {
	ch1 := make(chan DataEvent)
	ch2 := make(chan DataEvent)
	ch3 := make(chan DataEvent)

	eb.Subscribe("topic1", ch1)
	eb.Subscribe("topic2", ch2)
	eb.Subscribe("topic2", ch3)

	go publishTo("topic1", "Hi topic 1")
	go publishTo("topic2", "Welcome to topic 2")

	for {
		// We have used a select statement to get data from the quickest channel.
		select {
		case d := <-ch1:
			// Then it uses another goroutine for printout data. This is not necessary at all. But in some cases, you
			// have to do some heavy operation with the event. To prevent blocking the select we have used the goroutine.
			go printDataEvent("ch1", d)
		case d := <-ch2:
			go printDataEvent("ch2", d)
		case d := <-ch3:
			go printDataEvent("ch3", d)
		}
	}
}
