package equation

import (
	. "primitivo.fr/applinh/expert_system/hypothese"
)

type Equation struct {
	name       string
	Premisse   []Hypothese
	conclusion string
}

func (e Equation) FindFactInPrem(h Hypothese) int {
	for k, v := range e.Premisse {
		if v == h {
			return k
		}
	}
	return -1
}

func (e *Equation) RmFactOfPrem(h Hypothese) {
	i := e.FindFactInPrem(h)

	e.Premisse = append(e.Premisse[:i], e.Premisse[i+1:]...)
}

func NewEquation(name string, premisse []Hypothese, conclusion string) *Equation {
	n := Equation{name: name, Premisse: premisse, conclusion: conclusion}
	return &n
}

func (e *Equation) GetConclusion() string {
	return e.conclusion
}
