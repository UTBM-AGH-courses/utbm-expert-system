package models

type Hypothese struct {
	hypothese string
}

func NewHypothese(hypothese string) *Hypothese {
	n := Hypothese{hypothese: hypothese}
	return &n
}
