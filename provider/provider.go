package provider

import (
	"os"
	"sigs.k8s.io/kind/pkg/cmd"
	"sigs.k8s.io/kind/pkg/cmd/kind/create"
	"sigs.k8s.io/kind/pkg/cmd/kind/delete"
)

// https://github.com/kubernetes-sigs/kind/blob/main/cmd/kind/app/main.go

// Main is the kind main(), it will invoke Run(), if an error is returned
// it will then call os.Exit
func Main() {
	createCluster()
	deleteCluster()
}

func createCluster() {
	c := create.NewCommand(cmd.NewLogger(), cmd.StandardIOStreams())
	c.SetArgs([]string{"cluster"})
	if err := c.Execute(); err != nil {
		os.Exit(1)
	}
}

func deleteCluster(){
	c := delete.NewCommand(cmd.NewLogger(), cmd.StandardIOStreams())
	c.SetArgs([]string{"cluster"})
	if err := c.Execute(); err != nil {
		os.Exit(1)
	}
}
