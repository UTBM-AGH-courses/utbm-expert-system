package equation

import (
	"fmt"

	. "primitivo.fr/applinh/expert_system/hypothese"
)

type Equation struct {
	name       string
	Premisse   []Hypothese
	conclusion string
}

func (e Equation) FindHypInPrem(h Hypothese) int {
	for k, v := range e.Premisse {
		if v == h {
			return k
		}
	}
	return -1
}

func (e *Equation) RmHypOfPrem(h Hypothese) {
	i := e.FindHypInPrem(h)

	e.Premisse = append(e.Premisse[:i], e.Premisse[i+1:]...)
}

func NewEquation(name string, premisse []Hypothese, conclusion string) *Equation {
	n := Equation{name: name, Premisse: premisse, conclusion: conclusion}
	return &n
}

func NewEquation_Array(rules []map[string]interface{}) []Equation {
	equations := []Equation{}
	for _, v := range rules {

		h := make([]string, len(v["hypotheses"].([]interface{})))
		for k, val := range v["hypotheses"].([]interface{}) {
			h[k] = fmt.Sprint(val)
		}

		eq := *NewEquation(fmt.Sprintf("%v", v["name"]), NewHypothese_Array(h), fmt.Sprintf("%v", v["conclusion"]))
		equations = append(equations, eq)
	}
	return equations
}

func (e *Equation) GetConclusion() string {
	return e.conclusion
}
