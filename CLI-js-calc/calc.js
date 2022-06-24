function calculator() {
  var operation = prompt(
    "Please enter the mathematical operation you will like to use to continue \n + for addition \n - for subtraction \n * for multiplication \n / for division \n % for modulus"
  );

  if (
    operation === "+" ||
    operation === "-" ||
    operation === "*" ||
    operation === "/" ||
    operation === "%"
  ) {
    // numbers to be worked with by the user
    var num1 = parseInt(prompt("Enter your first number:\n"));
    var num2 = parseInt(prompt("Enter your second number:\n"));

    if (operation === "+") {
      // addition
      var result = num1 + num2;
      console.log(`${num1} + ${num2} = `, result);
    } else if (operation === "-") {
      // subtraction
      var result = num1 - num2;
      console.log(`${num1} - ${num2} = `, result);
    } else if (operation === "*") {
      // multiplication
      var result = num1 * num2;
      console.log(`${num1} * ${num2} = `, result);
    } else if (operation === "/") {
      // division
      var result = num1 / num2;
      console.log(`${num1} / ${num2} = `, result);
    } else if (operation === "%") {
      // modulus
      var result = num1 % num2;
      console.log(`${num1} % ${num2} = `, result);
    }
  } else {
    console.log("What you have entered is not a valid operator");
    calculator();
  }
}

calculator();
