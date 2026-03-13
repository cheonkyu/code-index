# 68. 타입 체크 (Type Checking)

안녕하세요! 코틀린 프로그래밍을 처음 배우는 분들을 위해 이번 챕터에서는 타입 체크에 대해 친절하게 설명해 드릴게요. 타입 체크는 코틀린에서 객체를 그 타입에 따라 다르게 다루는 데 매우 유용한 기능이에요. 특히 복잡한 객체 지향 설계에서 다양한 동작을 효과적으로 관리할 수 있게 도와줍니다. 이번에는 기본적인 개념부터 예제까지 차근차근 알아보도록 할게요.

## 핵심 개념 요약

1. **타입 체크의 목적**: 
   - 대부분의 경우에 대해 일반적인 동작을 정의하고, 특수한 경우에만 예외 처리를 하는 방식으로 코드를 간결하고 유지보수하기 쉽게 만드는 데 사용됩니다.
   - 모든 타입에 동일한 기능을 강제로 적용하는 대신, 특정 타입에만 해당하는 동작을 추가할 수 있어요.

2. **다형성과의 관계**:
   - 다형성 덕분에 기본 동작을 인터페이스나 추상 클래스에서 정의하고, 특정 타입에서는 예외 처리나 특수 동작을 추가할 수 있어요.

3. **`when` 표현식 활용**:
   - `when` 표현식은 특정 타입을 쉽게 판별하고 그에 맞는 동작을 수행할 수 있게 해줍니다. 이는 코드를 깔끔하게 유지하면서도 유연성을 제공해요.

## 예제 설명

### 곤충 예제 (`Insects.kt`)

#### 코드 예제
```kotlin
package typechecking
import atomictest.eq

// 인터페이스 정의
interface Insect {
    fun walk() = "$name: walk"
    fun fly() = "$name: fly"
}

// 클래스 구현
class HouseFly : Insect
class Flea : Insect {
    override fun fly() = throw Exception("Flea cannot fly")
    fun crawl() = "Flea: crawl"
}

// 기본 동작 메소드
fun Insect.basic() = 
    walk() + " " +
    if (this is Flea) crawl() else fly()

// 확장 인터페이스
interface SwimmingInsect : Insect {
    fun swim() = "$name: swim"
}
interface WaterWalker : Insect {
    fun walkWater() = "$name: walk on water"
}

// 구현 클래스
class WaterBeetle : SwimmingInsect
class WaterStrider : WaterWalker
class WhirligigBeetle : SwimmingInsect, WaterWalker

// 특정 타입에 대한 동작 선택
fun Insect.water() = 
    when(this) {
        is SwimmingInsect -> swim()
        is WaterWalker -> walkWater()
        else -> "$name: drown"
    }

// 메인 함수
fun main() {
    val insects = listOf(
        HouseFly(), Flea(), WaterStrider(), 
        WaterBeetle(), WhirligigBeetle()
    )
    println(insects.map { it.basic() }.toString()) // 출력 예시
    println(insects.map { it.water() }.toString()) // 출력 예시
}
```

**설명**:
- **`Insect` 인터페이스**는 모든 곤충이 공통적으로 가지고 있는 동작을 정의해요. `HouseFly`와 `Flea` 클래스는 이 인터페이스를 구현합니다.
- `Flea` 클래스는 `fly` 동작에서 예외를 발생시키고 대신 `crawl` 동작을 정의해요.
- `when` 표현식을 사용해 `Insect` 타입 내에서 특정 타입(`Flea`)에 대한 특수 동작(`crawl`)을 선택적으로 적용합니다.
- `water` 메소드에서도 유사한 방식으로 `SwimmingInsect`나 `WaterWalker` 타입에 특화된 동작을 선택적으로 수행합니다.

### 모양 예제 (`TypeCheck1.kt` 및 `TypeCheck2.kt`)

#### 코드 예제 (`TypeCheck1.kt`)
```kotlin
package typechecking
import atomictest.eq

// 인터페이스 정의
interface Shape {
    fun draw(): String
}

// 구현 클래스
class Circle : Shape {
    override fun draw() = "Circle: Draw"
}
class Square : Shape {
    override fun draw() = "Square: Draw"
    fun rotate() = "Square: Rotate"
}

// 특정 타입에 대한 동작 선택
fun turn(s: Shape) = when(s) {
    is Square -> s.rotate()
    else -> ""
}

// 메인 함수
fun main() {
    val shapes = listOf(Circle(), Square())
    println(shapes.map { it.draw() }.toString()) // 출력 예시
    println(shapes.map { turn(it) }.toString()) // 출력 예시
}
```

**설명**:
- `Shape` 인터페이스는 모든 모양이 공통적으로 가져야 할 동작(`draw`)을 정의합니다.
- `Square` 클래스는 `draw` 외에도 특수 동작인 `rotate`를 추가로 구현합니다.
- `turn` 함수에서는 `when` 표현식을 사용해 `Square` 타입에만 `rotate` 동작을 적용합니다. 이렇게 하면 인터페이스를 변경하지 않고도 특정 타입에 대한 특수 동작을 추가할 수 있어요.

#### 코드 예제 (`TypeCheck2.kt`)
```kotlin
package typechecking
import atomictest.eq

// 추가 클래스 구현
class Triangle : Shape {
    override fun draw() = "Triangle: Draw"
    fun rotate() = "Triangle: Rotate"
}

// 확장된 동작 선택 함수
fun turn2(s: Shape) = when(s) {
    is Square -> s.rotate() // 주의: 'Squ'는 오타 수정 필요
    is Triangle -> s.rotate()
    else -> ""
}

// 메인 함수
fun main() {
    val shapes = listOf(Circle(), Square(), Triangle())
    println(shapes.map { it.draw() }.toString()) // 출력 예시
    println(shapes.map { turn2(it) }.toString()) // 출력 예시
}
```

**설명**:
- `Triangle` 클래스를 추가하면서 `rotate` 동작을 구현했어요.
- `turn2` 함수에서는 `when` 표현식을 이용해 `Square`와 `Triangle` 타입에만 `rotate` 동작을 적용합니다. 이렇게 하면 시스템에 새로운 타입이 추가되어도 기존 코드에 영향을 주지 않으면서 유연하게 확장할 수 있어요.

## 마무리

타입 체크는 코드를 깔끔하고 유지보수하기 쉽게 만드는 데 매우 중요한 역할을 합니다. 특히 특수한 동작을 필요로 하는 특정 타입에 대해 예외 처리를 할 때 유용해요. 코틀린의 `when` 표현식을 활용하면 이런 복잡성을 효과적으로 관리할 수 있답니다. 앞으로도 다양한 예제를 통해 더 깊이 이해해 보도록 합시다! 질문이 있으면 언제든지 물어봐 주세요!