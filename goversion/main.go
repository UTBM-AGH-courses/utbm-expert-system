package main

import (
	"fmt"
)

type Fact struct {
	fact string
}

type Equation struct {
	name       string
	premisse   []Fact
	conclusion string
}

func (e Equation) findFactInPrem(f Fact) int {
	for k, v := range e.premisse {
		if v == f {
			return k
		}
	}
	return -1
}

func (e *Equation) rmFactOfPrem(f Fact) {
	i := e.findFactInPrem(f)

	e.premisse = append(e.premisse[:i], e.premisse[i+1:]...)
}

// func (e Equation) toStr() string {
// 	return e.name + " : " + e.premisse + " => " + e.conclusion

// }

type Systeme struct {
	eq []Equation
}

func main() {
	fmt.Println("Hello !")

	facts := []Fact{{fact: "A"}, {fact: "B"}}

	eq1 := Equation{name: "eq1", premisse: []Fact{{fact: "A"}, {fact: "B"}}, conclusion: "X"}
	eq2 := Equation{name: "eq2", premisse: []Fact{{fact: "D"}, {fact: "E"}}, conclusion: "Z"}

	systeme := Systeme{eq: []Equation{eq1, eq2}}

	for _, f := range facts {

		for key, eq := range systeme.eq {

			if eq.findFactInPrem(f) != -1 {

				eq.rmFactOfPrem(f)
				systeme.eq[key] = eq

				if len(eq.premisse) == 0 {

					facts = append(facts, Fact{fact: eq.conclusion})
				}
			}

		}
	}

	fmt.Println(facts)

}
