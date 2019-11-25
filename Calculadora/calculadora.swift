print("1° número: ")
var num1 = Double(readLine()!)!
print("Operação: ")
var op = readLine()!
print("2° número: ")
var num2 = Double(readLine()!)!

if op == "+"{
print(num1+num2)
}

if op == "-"{
print(num1-num2)
}

if op == "*"{
print(num1*num2)
}

if op == "/"{
print(num1/num2)
}

else {
print("Tá errado")
}