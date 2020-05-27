package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"os"
	"strings"

	. "primitivo.fr/applinh/expert_system/equation"
	. "primitivo.fr/applinh/expert_system/hypothese"
	. "primitivo.fr/applinh/expert_system/system"
)

func main() {
	a := os.Args
	arg1, _ := ioutil.ReadFile(a[1])

	// Lecture du fichier .json et récupération des informations
	var file = make(map[string]interface{})
	json.Unmarshal(arg1, &file)

	facts := file["facts"].([]interface{})
	rules := file["rules"].([]interface{})

	f := make([]string, len(facts))
	for k, v := range facts {
		f[k] = fmt.Sprint(v)
	}

	r := make([]map[string]interface{}, len(rules))
	for k, v := range rules {
		r[k] = v.(map[string]interface{})
	}

	// à partir du fichier .json :
	hypotheses := NewHypothese_Array(f) // Creation d'une liste d'objets hypotheses de départ
	equations := NewEquation_Array(r)   // Creation d'une liste d'objets equation
	systeme := NewSysteme(equations)    // Creation du systeme contenant des équations

	fmt.Println(strings.Repeat("*", 25))
	fmt.Println(" W E L C O M E")
	fmt.Println(strings.Repeat("*", 25))
	fmt.Println("Start : ")
	fmt.Println(hypotheses)
	fmt.Println("Systeme : ")
	fmt.Println(systeme)

	fmt.Println(strings.Repeat("*", 25))
	for i := 0; i < len(hypotheses); i++ {

		for key, eq := range systeme.Eq {

			if eq.FindHypInPrem(hypotheses[i]) != -1 { // si l'on trouve l'hypothèse courant dans les premisses de l'équation courante..

				eq.RmHypOfPrem(hypotheses[i]) // alors on la retire de l'équation courante
				systeme.Eq[key] = eq          // mise à jour de l'équation dans le système
				if len(eq.Premisse) == 0 {    // Lorsque qu'il n'y a plus de premisses...
					hypotheses = append(hypotheses, *NewHypothese(eq.GetConclusion())) // alors le système est résolu, et on peut ajouter la conclusion à la liste des faits
				}
			}

		}
	}
	fmt.Println("Facts : ")
	fmt.Println(hypotheses)

}
