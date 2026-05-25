#!/bin/bash
# Simple Calculator in Bash

echo "Select operation:"
echo "1. Add"
echo "2. Subtract"
echo "3. Multiply"
echo "4. Divide"

read -p "Enter choice (1/2/3/4): " choice
read -p "Enter first number: " num1
read -p "Enter second number: " num2

case $choice in
  1) result=$((num1 + num2)) ;;
  2) result=$((num1 - num2)) ;;
  3) result=$((num1 * num2)) ;;
  4) 
     if [ $num2 -eq 0 ]; then
       echo "Error! Division by zero."
       exit 1
     fi
     result=$((num1 / num2)) ;;
  *) echo "Invalid choice"; exit 1 ;;
esac

echo "Result: $result"

