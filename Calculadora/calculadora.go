package main
import "fmt"

func main() {

	number_one := askNumber("1° valor: ")

	operation  := askString("Operação: ") 

	number_two := askNumber("2° valor: ")

	result := calculate(number_one, number_two, operation)

	printResult(result)
}

func askString(msg string) string {
	var input string // declara a var input
	fmt.Print(msg) 	// apresenta a string Nome
  	fmt.Scanln(&input) // lê o que o usuário digitou
  	return input
}

func askNumber(msg string) float32 {
	var input float32 // declara a var input
	fmt.Print(msg) // apresenta a string Nome
  	fmt.Scanln(&input)  // lê o que o usuário digitou
  	return input
}

func calculate(n float32, m float32, op string) float32 {

	if (op == "+") {
		return n + m
	}

	if (op == "-") {
		return n - m
	}

	if (op == "*") {
		return n * m
	}

  return n / m
}

func printResult(number interface{}) {
	fmt.Printf("O resultado é: %v \n", number)
}

func isValidNumber(n float32) bool {
	return false
}

func isValidOperation(n string) bool {
	return false
}