a=int(input("Enter a value:"))
b=int(input("Enter a value:"))
let rec pow a b :=
    if b == 0 then 1
    else a *pow a (b-1)
