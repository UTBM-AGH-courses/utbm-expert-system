package models

import (
	. "primitivo.fr/applinh/expert_system/equation"
)

type Systeme struct {
	Eq []Equation
}

func NewSysteme(eq []Equation) *Systeme {
	s := Systeme{Eq: eq}
	return &s
}
