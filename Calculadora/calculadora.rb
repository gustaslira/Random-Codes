print '1° valor: '
a = gets.to_i

print 'Operação: '
op = gets.chomp    
      
print '2° valor: '
b = gets.to_i

if op == '+'
x = a + b
print x
end

if op == '-'
x = a - b
print x
end

if op == '*'
x = a * b
print x
end

if op == '/'
x = a / b
print x
end
