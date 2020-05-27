package models

type Hypothese struct {
	hypothese string
}

func NewHypothese(hypothese string) *Hypothese {
	n := Hypothese{hypothese: hypothese}
	return &n
}

func NewHypothese_Array(hyp []string) []Hypothese {

	hypotheses := []Hypothese{}
	for _, v := range hyp {
		hyp := *NewHypothese(v)
		hypotheses = append(hypotheses, hyp)
	}
	return hypotheses
}
