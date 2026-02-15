def Calculator():
    # Calculator Program
    print("\033[1mCalculator Program Welcome!\033[0m")
    #logic
    def add(*nums):
        "This func is used to addition numaricals"
        total = nums[0]
        for num in nums[1:]:
            total += num
        return total

    def sub(*nums):
        "This func is used to subtract numaricals"
        total = nums[0]
        for num in nums[1:]:
            total -= num
        return total

    def multiply(*nums):
        "This func is used to multiply numaricals"
        total = nums[0]
        for num in nums[1:]:
            total *= num
        return total

    def division(*nums):
        "This func is used to divide numaricals"
        total = nums[0]
        for num in nums[1:]:
            total /= num
        return total


    while True:  
        n1 = int(input("Enter a number: "))
        n2 = int(input("Enter another number: "))

        #add
        addition = add(n1, n2)

        #sub
        substration = sub(n1, n2)

        #multiply
        multiply_r = multiply(n1, n2)

        #division
        division_r = division(n1, n2)

        #choose
        choose = input("Choose the operation: ")
        if choose == "Add".lower() or choose == "Add":
            print(addition)
        elif choose == "Sub".lower() or choose == "Sub":
            print(substration)
        elif choose == "Multiply".lower() or choose == "Multiply":
            print(multiply_r)
        elif choose == "Divide".lower() or choose == "Divide":
            print(division_r)
if __name__ == "__main__":  
    Calculator()