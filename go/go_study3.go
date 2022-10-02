package main

import "fmt"
import "math"

type Vertex struct {
	X, Y float64
}

func (v Vertex) Abs() float64 {
	return math.Sqrt(x.X*v.X + v.Y * v.Y)
}

func (v *Vertex) Scale(f float64) {
	v.X = v.X * f
	v.Y = v.Y * f
}

func main() {
	v := Vertex{3, 4}
	v.Scale(10) // 여기 Scale앞에 v.가 붙어있음 이게 리시버라고 함. 
	fmt.Println(v.Abs())
}

