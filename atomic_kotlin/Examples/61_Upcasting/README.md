# 61. Upcasting: 객체를 더 일반적인 유형으로 취급하기

안녕하세요! 오늘은 코틀린 프로그래밍에서 중요한 개념 중 하나인 **Upcasting**(상위 타입으로의 캐스팅)에 대해 배워볼게요. 초보자분들도 쉽게 이해할 수 있도록 자세히 설명해 드릴게요.

## 기본 개념 이해하기

**Upcasting**이란 특정 객체를 그 객체의 상위 타입(기본 타입)으로 취급하는 것을 의미해요. 쉽게 말해, 작은 개를 동물이라는 큰 범주로 묶는 것과 비슷하죠. 상속 구조를 생각해보면, 기본 클래스가 맨 위에 있고 그 아래로 파생 클래스들이 펼쳐져 있는 모습을 떠올릴 수 있어요.

### 코틀린에서의 적용

코틀린은 자바와 달리 모든 것을 클래스로 묶을 필요가 없어요. 대신 확장 함수를 사용해서 추가적인 기능을 붙일 수 있죠. 하지만 상속은 의도적으로 사용해야 해요. 이를 통해 코드의 재사용성을 높일 수 있는 추상화를 제공해요.

### 예제 코드로 이해하기

아래 예제 코드를 보면서 이해해봅시다. `Shape` 인터페이스를 기반으로 `Circle`, `Square`, `Triangle` 클래스를 정의해 볼게요.

#### Shape 인터페이스 정의

```kotlin
package upcasting

// Shape 인터페이스 정의
interface Shape {
    fun draw(): String
    fun erase(): String
}
```

#### Shape 클래스 구현

```kotlin
class Circle : Shape {
    override fun draw() = "Circle.draw"
    override fun erase() = "Circle.erase"
}

class Square : Shape {
    override fun draw() = "Square.draw"
    override fun erase() = "Square.erase"
    fun color() = "Square.color"  // Square만의 추가 기능
}

class Triangle : Shape {
    override fun draw() = "Triangle.draw"
    override fun erase() = "Triangle.erase"
    fun rotate() = "Triangle.rotate"  // Triangle만의 추가 기능
}
```

#### 업캐스팅을 사용하는 함수

```kotlin
// show 함수: Shape 타입의 객체를 받아서 draw 메소드를 호출
package upcasting

import atomictest.*

fun show(shape: Shape) {
    trace("Show: ${shape.draw()}")
}

fun main() {
    // Circle, Square, Triangle 객체 리스트 생성
    val shapes = listOf(Circle(), Square(), Triangle())
    
    // 각 객체를 show 함수에 전달
    shapes.forEach { ::show }
    
    // 예상 출력 결과
    traceEquals("""
    Show: Circle.draw
    Show: Square.draw
    Show: Triangle.draw
    """)
}
```

### 핵심 개념 요약

1. **상위 타입으로 취급하기 (Upcasting)**:
   - 특정 객체를 그 객체의 상위 타입(기본 타입)으로 취급합니다.
   - 예를 들어, `Circle`, `Square`, `Triangle`을 모두 `Shape` 타입으로 전달할 수 있어요.

2. **다형성의 이점**:
   - 코드 재사용성 향상: `show()` 함수 하나로 다양한 모양 객체를 처리할 수 있어요.
   - 특정 기능 제한 (Liskov Substitution Principle): 상위 타입으로 업캐스팅하면 추가된 기능은 사용할 수 없어요. 예를 들어, `Square`의 `color()` 함수는 `show()` 함수에서는 사용할 수 없어요.

3. **의도적인 상속 사용**:
   - 상속은 필요할 때만 사용하세요. 무분별한 상속은 코드를 복잡하게 만들 수 있어요. 대신 기능 확장은 확장 함수를 활용하는 것이 더 효과적일 수 있어요.

이렇게 업캐스팅을 이해하면 코틀린에서 상속과 다형성을 효과적으로 활용할 수 있게 돼요. 궁금한 점이 있으면 언제든지 물어봐주세요!