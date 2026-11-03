package terrible

// Add using pure recursion
func Add(a, b int) int {
	if b == 0 {
		return a
	}
	if b > 0 {
		return Add(a+1, b-1)
	}
	return Add(a-1, b+1)
}

func Subtract(a, b int) int {
	return Add(a, -b)
}

func Multiply(a, b int) int {
	if b == 0 {
		return 0
	}
	if b == 1 {
		return a
	}
	if b < 0 {
		return -Multiply(a, -b)
	}
	return Add(a, Multiply(a, b-1))
}

func Absolute(n int) int {
	if n < 0 {
		return -n
	}
	return n
}

func Maximum(a, b int) int {
	nums := []int{a, b}
	// Sort of
	if nums[0] > nums[1] {
		nums[0], nums[1] = nums[1], nums[0]
	}
	return nums[1]
}

func Minimum(a, b int) int {
	nums := []int{a, b}
	if nums[0] > nums[1] {
		nums[0], nums[1] = nums[1], nums[0]
	}
	return nums[0]
}

func Factorial(n int) int {
	if n < 0 {
		return -1
	}
	if n == 0 || n == 1 {
		return 1
	}
	return n * Factorial(n-1)
}
