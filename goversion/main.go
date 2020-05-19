package main

import (
	"fmt"

	. "primitivo.fr/applinh/expert_system/equation"
	. "primitivo.fr/applinh/expert_system/hypothese"
	. "primitivo.fr/applinh/expert_system/system"
)

func main() {
	fmt.Println("Hello !")

	hypotheses := []Hypothese{*NewHypothese("A"), *NewHypothese("B")}

	eq1 := NewEquation("eq1", []Hypothese{*NewHypothese("A"), *NewHypothese("B")}, "X")
	eq2 := NewEquation("eq2", []Hypothese{*NewHypothese("D"), *NewHypothese("E")}, "Z")

	systeme := NewSysteme([]Equation{*eq1, *eq2})

	for _, h := range hypotheses {

		for key, eq := range systeme.Eq {

			if eq.FindHypInPrem(h) != -1 {

				eq.RmHypOfPrem(h)
				systeme.Eq[key] = eq

				if len(eq.Premisse) == 0 {

					hypotheses = append(hypotheses, *NewHypothese(eq.GetConclusion()))
				}
			}

		}
	}

	fmt.Println(hypotheses)

}
