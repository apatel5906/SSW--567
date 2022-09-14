# Arpit Patel
#The following code is for the test cases for the traingle program.
import pytest
from Triangle import classify_triangle

class TestClass:

    def test_case1(self):
        print("Test for Equilateral triangle\n")
        assert classify_triangle(1, 1, 1) == "Equilateral"

    def test_case2(self):
        print("Test for Equilateral triangle\n")
        assert classify_triangle(9, 9, 9) == "Equilateral"

    def test_case3(self):
        print("Test for Equilateral triangle\n")
        assert classify_triangle(2, 2, 2) == "Equilateral"

    def test_case4(self):
        print("Test for Equilateral triangle\n")
        assert classify_triangle(6, 6, 6) == "Equilateral"


    def test_case5(self):
        print("Test for Isosceles triangle\n")
        assert classify_triangle(3, 3, 2) == "Isosceles"

    def test_case6(self):
        print("Test for Isosceles triangle\n")
        assert classify_triangle(4, 5, 5) == "Isosceles"

    def test_case7(self):
        print("Test for Isosceles triangle\n")
        assert classify_triangle(4, 3, 4) == "Isosceles"

    def test_case8(self):
        print("Test for Scalene triangle\n")
        assert classify_triangle(3, 6, 7) == "Scalene"

    def test_case9(self):
        print("Test for Scalene triangle\n")
        assert classify_triangle(11, 14, 23) == "Scalene"

    def test_case10(self):
        print("Test for Scalene triangle\n")
        assert classify_triangle(12, 13, 14) == "Scalene"

    def test_case11(self):
        print("Test for Scalene triangle\n")
        assert classify_triangle(18, 19, 26) == "Scalene"

    def test_case12(self):
        print("Test for Right triangle\n")
        assert classify_triangle(3, 4, 5) == "Right"

    def test_case13(self):
        print("Test for Right triangle\n")
        assert classify_triangle(17, 15, 8) == "Right"

    def test_case14(self):
        print("Test for Right triangle\n")
        assert classify_triangle(7, 24, 25) == "Right"

    def test_case15(self):
        print("Test for invalid triangle\n")
        assert classify_triangle(1, 2, 10) == "Not a Triangle"

    def test_case16(self):
        print("Test for invalid triangle\n")
        assert classify_triangle(5, 4, 11) == "Not a Triangle"

    def test_case17(self):
        print("Test for invalid triangle\n")
        assert classify_triangle(2, 2, 10) == "Not a Triangle"

    def test_case18(self):
        print("Test for Negative sides\n")
        assert classify_triangle(-5, -4, -3) == "Invalid Input"

    def test_case19(self):
        print("Test for invalid triangle\n")
        assert classify_triangle(0, 0, 0) == "Invalid Input"

    def test_case20(self):
        print("Test for invalid triangle\n")
        assert classify_triangle(0.1, 0.2, 0.3) == "Invalid Input"

if __name__ == '__main__':
    print('Running test cases')
    pytest.main()

