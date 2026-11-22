
import math

history_data = []

print("*********************** Advanced Calculator ***************************")
print("Select function:")
print("1. Basic Arithmetic")
print("2. Trigonometric Functions")
print("3. Exponential and Logarithm")
print("4. Factorial")
print("5. Derivative")
print("6. Second Derivative")
print("7. Definite Integral")
print("8. Unit Conversion")
print("9. Quadratic Solver")
print("10. Number Theory")
print("11. Statistics")
print("12. Polynomial Derivative")
print("13. Newton-Raphson")
print("14. Bisection")
print("15. History")
print("16. Exit")
print("************************************************************************")

while True:

    choice = input("\nEnter choice (1-16): ")

    # ==================================================
    # 1. BASIC ARITHMETIC
    # ==================================================

    if choice == '1':

        print("\nSelect operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Modulus")
        print("6. Exponentiation")
        print("7. Floor Division")

        operation = input("Enter operation (1-7): ")

        if operation in ['1', '2', '3', '4', '5', '6', '7']:

            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if operation == '1':
                result = num1 + num2
                print(f"{num1} + {num2} = {result}")

            elif operation == '2':
                result = num1 - num2
                print(f"{num1} - {num2} = {result}")

            elif operation == '3':
                result = num1 * num2
                print(f"{num1} * {num2} = {result}")

            elif operation == '4':
                if num2 != 0:
                    result = num1 / num2
                    print(f"{num1} / {num2} = {result}")
                else:
                    print("Error: Division by zero.")

            elif operation == '5':
                if num2 != 0:
                    result = num1 % num2
                    print(f"{num1} % {num2} = {result}")
                else:
                    print("Error: Modulus by zero.")

            elif operation == '6':
                result = num1 ** num2
                print(f"{num1} ** {num2} = {result}")

            elif operation == '7':
                if num2 != 0:
                    result = num1 // num2
                    print(f"{num1} // {num2} = {result}")
                else:
                    print("Error: Floor division by zero.")

            if operation != '4' or num2 != 0:
                history_data.append(f"Arithmetic result: {result}")

        else:
            print("Invalid operation.")

    # ==================================================
    # 2. TRIGONOMETRIC FUNCTIONS
    # ==================================================

    elif choice == '2':

        print("\nSelect trigonometric function:")
        print("1. Sine")
        print("2. Cosine")
        print("3. Tangent")
        print("4. Cosecant")
        print("5. Secant")
        print("6. Cotangent")

        operation = input("Enter operation (1-6): ")

        if operation in ['1', '2', '3', '4', '5', '6']:

            angle = float(input("Enter angle in degrees: "))
            radians = math.radians(angle)

            if operation == '1':
                result = math.sin(radians)
                print(f"sin({angle}) = {result}")

            elif operation == '2':
                result = math.cos(radians)
                print(f"cos({angle}) = {result}")

            elif operation == '3':
                result = math.tan(radians)
                print(f"tan({angle}) = {result}")

            elif operation == '4':
                value = math.sin(radians)

                if abs(value) > 0.000000000001:
                    result = 1 / value
                    print(f"csc({angle}) = {result}")
                else:
                    print("Cosecant is undefined.")

            elif operation == '5':
                value = math.cos(radians)

                if abs(value) > 0.000000000001:
                    result = 1 / value
                    print(f"sec({angle}) = {result}")
                else:
                    print("Secant is undefined.")

            elif operation == '6':
                value = math.sin(radians)

                if abs(value) > 0.000000000001:
                    result = math.cos(radians) / value
                    print(f"cot({angle}) = {result}")
                else:
                    print("Cotangent is undefined.")

            history_data.append(f"Trigonometric result: {result}")

        else:
            print("Invalid operation.")

    # ==================================================
    # 3. EXPONENTIAL AND LOGARITHM
    # ==================================================

    elif choice == '3':

        print("\nSelect operation:")
        print("1. Exponential")
        print("2. Natural Logarithm")
        print("3. Logarithm Base 10")

        operation = input("Enter operation (1-3): ")

        if operation in ['1', '2', '3']:

            num = float(input("Enter number: "))

            if operation == '1':
                result = math.exp(num)
                print(f"e^{num} = {result}")

            elif operation == '2':
                if num > 0:
                    result = math.log(num)
                    print(f"ln({num}) = {result}")
                else:
                    print("Natural logarithm requires a positive number.")

            elif operation == '3':
                if num > 0:
                    result = math.log10(num)
                    print(f"log10({num}) = {result}")
                else:
                    print("Logarithm requires a positive number.")

            if operation == '1' or num > 0:
                history_data.append(f"Logarithm result: {result}")

        else:
            print("Invalid operation.")

    # ==================================================
    # 4. FACTORIAL
    # ==================================================

    elif choice == '4':

        num = int(input("Enter a non-negative integer: "))

        if num >= 0:
            result = math.factorial(num)
            print(f"{num}! = {result}")

            history_data.append(f"{num}! = {result}")

        else:
            print("Factorial is undefined for negative numbers.")

    # ==================================================
    # 5. FIRST DERIVATIVE
    # ==================================================

    elif choice == '5':

        n = int(input("How many functions do you want to differentiate? "))

        for i in range(n):

            print("\nFunction", i + 1)

            expression = input("Enter function (example: x**2): ")
            x = float(input("Enter value of x: "))

            h = 0.00001

            allowed_names = {
                "x": x + h,
                "sin": math.sin,
                "cos": math.cos,
                "tan": math.tan,
                "sqrt": math.sqrt,
                "log": math.log,
                "log10": math.log10,
                "exp": math.exp,
                "pi": math.pi,
                "e": math.e,
                "abs": abs
            }

            fx1 = eval(expression, {"__builtins__": {}}, allowed_names)

            allowed_names["x"] = x - h

            fx2 = eval(expression, {"__builtins__": {}}, allowed_names)

            result = (fx1 - fx2) / (2 * h)

            print("Derivative at x =", x, "is", result)

            history_data.append(
                f"Derivative of {expression} at x={x}: {result}"
            )

    # ==================================================
    # 6. SECOND DERIVATIVE
    # ==================================================

    elif choice == '6':

        n = int(input("How many functions do you want to differentiate? "))

        for i in range(n):

            print("\nFunction", i + 1)

            expression = input("Enter function (example: x**2): ")
            x = float(input("Enter value of x: "))

            h = 0.001

            allowed_names = {
                "x": x,
                "sin": math.sin,
                "cos": math.cos,
                "tan": math.tan,
                "sqrt": math.sqrt,
                "log": math.log,
                "log10": math.log10,
                "exp": math.exp,
                "pi": math.pi,
                "e": math.e,
                "abs": abs
            }

            allowed_names["x"] = x + h
            fx1 = eval(expression, {"__builtins__": {}}, allowed_names)

            allowed_names["x"] = x
            fx = eval(expression, {"__builtins__": {}}, allowed_names)

            allowed_names["x"] = x - h
            fx2 = eval(expression, {"__builtins__": {}}, allowed_names)

            result = (fx1 - 2 * fx + fx2) / (h ** 2)

            print("Second derivative at x =", x, "is", result)

            history_data.append(
                f"Second derivative of {expression} at x={x}: {result}"
            )

    # ==================================================
    # 7. DEFINITE INTEGRAL
    # ==================================================

    elif choice == '7':

        expression = input("Enter function (example: x**2): ")

        lower_limit = float(input("Enter lower limit: "))
        upper_limit = float(input("Enter upper limit: "))

        intervals = 1000
        h = (upper_limit - lower_limit) / intervals

        allowed_names = {
            "x": lower_limit,
            "sin": math.sin,
            "cos": math.cos,
            "tan": math.tan,
            "sqrt": math.sqrt,
            "log": math.log,
            "log10": math.log10,
            "exp": math.exp,
            "pi": math.pi,
            "e": math.e,
            "abs": abs
        }

        allowed_names["x"] = lower_limit
        first_value = eval(expression, {"__builtins__": {}}, allowed_names)

        allowed_names["x"] = upper_limit
        last_value = eval(expression, {"__builtins__": {}}, allowed_names)

        result = first_value + last_value

        for i in range(1, intervals):

            x = lower_limit + i * h

            allowed_names["x"] = x

            value = eval(expression, {"__builtins__": {}}, allowed_names)

            if i % 2 == 0:
                result = result + 2 * value
            else:
                result = result + 4 * value

        result = result * h / 3

        print(
            f"Definite integral of {expression} "
            f"from {lower_limit} to {upper_limit} = {result}"
        )

        history_data.append(f"Integral result: {result}")

    # ==================================================
    # 8. UNIT CONVERSION
    # ==================================================

    elif choice == '8':

        print("\nSelect conversion type:")
        print("1. Length")
        print("2. Mass")
        print("3. Temperature")

        conversion_type = input("Enter conversion type (1-3): ")

        if conversion_type == '1':

            print("\n1. Meter to Kilometer")
            print("2. Kilometer to Meter")
            print("3. Meter to Centimeter")
            print("4. Centimeter to Meter")
            print("5. Kilometer to Mile")
            print("6. Mile to Kilometer")

            operation = input("Enter operation (1-6): ")
            value = float(input("Enter value: "))

            if operation == '1':
                result = value / 1000
            elif operation == '2':
                result = value * 1000
            elif operation == '3':
                result = value * 100
            elif operation == '4':
                result = value / 100
            elif operation == '5':
                result = value * 0.621371
            elif operation == '6':
                result = value / 0.621371
            else:
                print("Invalid conversion.")
                result = None

            if result is not None:
                print("Converted value:", result)
                history_data.append(f"Length conversion: {result}")

        elif conversion_type == '2':

            print("\n1. Kilogram to Gram")
            print("2. Gram to Kilogram")
            print("3. Kilogram to Pound")
            print("4. Pound to Kilogram")

            operation = input("Enter operation (1-4): ")
            value = float(input("Enter value: "))

            if operation == '1':
                result = value * 1000
            elif operation == '2':
                result = value / 1000
            elif operation == '3':
                result = value * 2.20462
            elif operation == '4':
                result = value / 2.20462
            else:
                print("Invalid conversion.")
                result = None

            if result is not None:
                print("Converted value:", result)
                history_data.append(f"Mass conversion: {result}")

        elif conversion_type == '3':

            print("\n1. Celsius to Fahrenheit")
            print("2. Fahrenheit to Celsius")
            print("3. Celsius to Kelvin")
            print("4. Kelvin to Celsius")

            operation = input("Enter operation (1-4): ")
            value = float(input("Enter temperature: "))

            if operation == '1':
                result = (value * 9 / 5) + 32
            elif operation == '2':
                result = (value - 32) * 5 / 9
            elif operation == '3':
                result = value + 273.15
            elif operation == '4':
                result = value - 273.15
            else:
                print("Invalid conversion.")
                result = None

            if result is not None:
                print("Converted temperature:", result)
                history_data.append(f"Temperature conversion: {result}")

        else:
            print("Invalid conversion type.")

    # ==================================================
    # 9. QUADRATIC SOLVER
    # ==================================================

    elif choice == '9':

        print("\nQuadratic Equation: ax**2 + bx + c = 0")

        a = float(input("Enter coefficient a: "))
        b = float(input("Enter coefficient b: "))
        c = float(input("Enter coefficient c: "))

        if a == 0:
            print("Coefficient a cannot be zero.")

        else:

            d = (b ** 2) - (4 * a * c)

            if d > 0:

                sol1 = (-b + math.sqrt(d)) / (2 * a)
                sol2 = (-b - math.sqrt(d)) / (2 * a)

                print("Two real and distinct roots:")
                print("Root 1:", sol1)
                print("Root 2:", sol2)

            elif d == 0:

                sol = -b / (2 * a)

                print("Two equal real roots:")
                print("Root:", sol)

            else:

                real = -b / (2 * a)
                imaginary = math.sqrt(-d) / abs(2 * a)

                print("Two complex roots:")
                print(f"Root 1: {real} + {imaginary}i")
                print(f"Root 2: {real} - {imaginary}i")

            history_data.append("Quadratic equation solved.")

    # ==================================================
    # 10. NUMBER THEORY
    # ==================================================

    elif choice == '10':

        print("\nSelect operation:")
        print("1. Prime Check")
        print("2. GCD")
        print("3. LCM")

        operation = input("Enter operation (1-3): ")

        if operation == '1':

            num = int(input("Enter number: "))

            if num > 1:

                for i in range(2, int(math.sqrt(num)) + 1):

                    if num % i == 0:
                        print(num, "is not a prime number.")
                        break

                else:
                    print(num, "is a prime number.")

            else:
                print(num, "is not a prime number.")

        elif operation == '2':

            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))

            result = math.gcd(num1, num2)

            print("GCD:", result)

        elif operation == '3':

            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))

            if num1 == 0 or num2 == 0:
                result = 0
            else:
                result = abs(num1 * num2) // math.gcd(num1, num2)

            print("LCM:", result)

        else:
            print("Invalid operation.")

    # ==================================================
    # 11. STATISTICS
    # ==================================================

    elif choice == '11':

        print("\nSelect operation:")
        print("1. Mean")
        print("2. Median")
        print("3. Mode")
        print("4. Standard Deviation")

        operation = input("Enter operation (1-4): ")

        if operation in ['1', '2', '3', '4']:

            data = input("Enter numbers separated by spaces: ")
            data_list = list(map(float, data.split()))

            size = len(data_list)

            if size == 0:
                print("No numbers entered.")

            elif operation == '1':

                total = 0

                for num in data_list:
                    total = total + num

                result = total / size

                print("Mean:", result)
                history_data.append(f"Mean: {result}")

            elif operation == '2':

                data_list.sort()

                if size % 2 == 0:
                    middle1 = data_list[size // 2 - 1]
                    middle2 = data_list[size // 2]

                    result = (middle1 + middle2) / 2

                else:
                    result = data_list[size // 2]

                print("Median:", result)
                history_data.append(f"Median: {result}")

            elif operation == '3':

                highest_count = 0
                modes = []

                for num in data_list:

                    count = 0

                    for value in data_list:
                        if value == num:
                            count = count + 1

                    if count > highest_count:
                        highest_count = count
                        modes = [num]

                    elif count == highest_count and num not in modes:
                        modes.append(num)

                if highest_count == 1:
                    print("No mode found.")

                else:
                    print("Mode:", modes)
                    history_data.append(f"Mode: {modes}")

            elif operation == '4':

                if size < 2:
                    print("At least two numbers are required.")

                else:

                    total = 0

                    for num in data_list:
                        total = total + num

                    mean = total / size
                    squared_difference = 0

                    for num in data_list:
                        squared_difference += (num - mean) ** 2

                    result = math.sqrt(squared_difference / (size - 1))

                    print("Standard Deviation:", result)
                    history_data.append(f"Standard deviation: {result}")

        else:
            print("Invalid operation.")

    # ==================================================
    # 12. POLYNOMIAL DERIVATIVE
    # ==================================================

    elif choice == '12':

        expression = input(
            "Enter polynomial (example: x**3 + 2*x**2 + x + 1): "
        )

        x = float(input("Enter value of x: "))
        h = 0.00001

        allowed_names = {
            "x": x + h,
            "sin": math.sin,
            "cos": math.cos,
            "tan": math.tan,
            "sqrt": math.sqrt,
            "log": math.log,
            "log10": math.log10,
            "exp": math.exp,
            "pi": math.pi,
            "e": math.e,
            "abs": abs
        }

        fx1 = eval(expression, {"__builtins__": {}}, allowed_names)

        allowed_names["x"] = x - h

        fx2 = eval(expression, {"__builtins__": {}}, allowed_names)

        result = (fx1 - fx2) / (2 * h)

        print("Derivative at x =", x, "is", result)
        print("Note: This is a numerical derivative.")

        history_data.append(f"Polynomial derivative: {result}")

    # ==================================================
    # 13. NEWTON-RAPHSON METHOD
    # ==================================================

    elif choice == '13':

        expression = input("Enter function (example: x**2 - 2): ")

        initial_guess = float(input("Enter initial guess: "))
        tolerance = float(input("Enter tolerance: "))
        max_iterations = int(input("Enter maximum iterations: "))

        current_guess = initial_guess
        h = 0.00001

        allowed_names = {
            "x": current_guess,
            "sin": math.sin,
            "cos": math.cos,
            "tan": math.tan,
            "sqrt": math.sqrt,
            "log": math.log,
            "log10": math.log10,
            "exp": math.exp,
            "pi": math.pi,
            "e": math.e,
            "abs": abs
        }

        for iteration in range(max_iterations):

            allowed_names["x"] = current_guess
            f_value = eval(expression, {"__builtins__": {}}, allowed_names)

            allowed_names["x"] = current_guess + h
            fx1 = eval(expression, {"__builtins__": {}}, allowed_names)

            allowed_names["x"] = current_guess - h
            fx2 = eval(expression, {"__builtins__": {}}, allowed_names)

            derivative_value = (fx1 - fx2) / (2 * h)

            if abs(derivative_value) < 0.000000000001:
                print("Derivative is zero. Cannot continue.")
                break

            next_guess = current_guess - (f_value / derivative_value)

            if abs(next_guess - current_guess) < tolerance:

                print("Root found:", next_guess)
                print("Iterations:", iteration + 1)

                history_data.append(f"Newton-Raphson root: {next_guess}")
                break

            current_guess = next_guess

        else:
            print("Maximum iterations reached.")
            print("Approximate root:", current_guess)

    # ==================================================
    # 14. BISECTION METHOD
    # ==================================================

    elif choice == '14':

        expression = input("Enter function (example: x**3 - x - 2): ")

        lower_bound = float(input("Enter lower bound: "))
        upper_bound = float(input("Enter upper bound: "))

        tolerance = float(input("Enter tolerance: "))
        max_iterations = int(input("Enter maximum iterations: "))

        allowed_names = {
            "x": lower_bound,
            "sin": math.sin,
            "cos": math.cos,
            "tan": math.tan,
            "sqrt": math.sqrt,
            "log": math.log,
            "log10": math.log10,
            "exp": math.exp,
            "pi": math.pi,
            "e": math.e,
            "abs": abs
        }

        allowed_names["x"] = lower_bound
        f_lower = eval(expression, {"__builtins__": {}}, allowed_names)

        allowed_names["x"] = upper_bound
        f_upper = eval(expression, {"__builtins__": {}}, allowed_names)

        if f_lower == 0:
            print("Root found:", lower_bound)

        elif f_upper == 0:
            print("Root found:", upper_bound)

        elif f_lower * f_upper > 0:
            print("Bisection requires a sign change over the interval.")

        else:

            for iteration in range(max_iterations):

                midpoint = (lower_bound + upper_bound) / 2

                allowed_names["x"] = midpoint
                f_midpoint = eval(
                    expression,
                    {"__builtins__": {}},
                    allowed_names
                )

                if abs(f_midpoint) < tolerance or (upper_bound - lower_bound) / 2 < tolerance:

                    print("Root found:", midpoint)
                    print("Iterations:", iteration + 1)

                    history_data.append(f"Bisection root: {midpoint}")
                    break

                if f_lower * f_midpoint < 0:
                    upper_bound = midpoint
                    f_upper = f_midpoint

                else:
                    lower_bound = midpoint
                    f_lower = f_midpoint

            else:
                print("Maximum iterations reached.")
                print("Approximate root:", (lower_bound + upper_bound) / 2)

    # ==================================================
    # 15. HISTORY
    # ==================================================

    elif choice == '15':

        print("\nDisplaying Calculation History")
        print("--------------------------------")

        if len(history_data) > 0:

            for item in history_data:
                print(item)

        else:
            print("No calculation history available.")

    # ==================================================
    # 16. EXIT
    # ==================================================

    elif choice == '16':

        print("Exit")
        break

    else:

        print("Invalid input. Please enter a number between 1 and 16.")
