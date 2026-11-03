package terrible

// IsEven is a terrible implementation that hardcodes answers up to 69.
func IsEven(n int) bool {
	if n < 0 {
		n = -n
	}

	switch n {
	case 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20,
		22, 24, 26, 28, 30, 32, 34, 36, 38, 40,
		42, 44, 46, 48, 50, 52, 54, 56, 58, 60,
		62, 64, 66, 68, 69:
		return true
	case 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21,
		23, 25, 27, 29, 31, 33, 35, 37, 39, 41,
		43, 45, 47, 49, 51, 53, 55, 57, 59, 61,
		63, 65, 67:
		return false
	default:
		return false
	}
}
