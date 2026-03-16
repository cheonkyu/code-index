# Item 39: 태그 기반 클래스 대신 상속 구조 사용하기

## 핵심 가이드라인 및 이유 (Best Practice)

Effective Kotlin에서 제시하는 이 가이드라인은 코드의 가독성과 유지보수성을 향상시키는 데 중점을 둡니다. 태그 기반 클래스(tagged classes) 대신 상속 구조를 활용하는 것이 권장됩니다. 이 접근법은 다음과 같은 이점이 있습니다:

- **확장성 향상**: 상속 구조를 사용하면 새로운 기능이나 속성을 추가하는 것이 더 쉬워집니다. 기존 클래스에 새로운 하위 클래스를 쉽게 추가할 수 있습니다.
- **코드 가독성**: 상속 관계는 클래스 간의 관계를 명확하게 보여주므로 코드의 이해도를 높입니다. 상속 구조는 타입 계층을 명확히 표현하여 개발자가 클래스 역할을 쉽게 파악할 수 있게 합니다.
- **다형성의 활용**: 상속을 통해 다형성을 효과적으로 활용할 수 있어, 동일한 인터페이스로 다양한 행동을 처리할 수 있게 됩니다.

## 예제 코드

다음은 태그 기반 클래스 대신 상속 구조를 사용하는 예제입니다:

### 태그 기반 클래스 예시
```kotlin
// 태그 기반 클래스 예시 (추천하지 않음)
abstract class Vehicle {
    abstract fun drive()
}

class Car : Vehicle {
    override fun drive() {
        println("Car is driving")
    }
}

class Bike : Vehicle {
    override fun drive() {
        println("Bike is riding")
    }
}

// 사용 예시
fun useVehicle(v: Vehicle) {
    v.drive() // 타입 안전성 문제 가능성
}

fun main() {
    val car = Car()
    val bike = Bike()
    useVehicle(car)  // 정상 동작
    useVehicle(bike) // 정상 동작 (타입 안전성에 주의 필요)
}
```

### 상속 구조 예시
```kotlin
// 상속 구조 예시 (추천)
abstract class Vehicle {
    abstract fun drive()
}

class Car : Vehicle() {
    override fun drive() {
        println("Car is driving")
    }
}

class Bike : Vehicle() {
    override fun drive() {
        println("Bike is riding")
    }
}

// 확장성 향상 예시: 새로운 타입 추가
class ElectricCar : Car() {
    override fun drive() {
        println("Electric Car is driving quietly")
    }
}

// 사용 예시
fun useVehicle(v: Vehicle) {
    v.drive() // 타입 안전성 유지
}

fun main() {
    val car = Car()
    val bike = Bike()
    val electricCar = ElectricCar()
    useVehicle(car)  // 정상 동작
    useVehicle(bike) // 정상 동작
    useVehicle(electricCar)  // 새로운 타입도 쉽게 처리 가능
}
```

### 설명
- **상속 구조 예시**에서는 `ElectricCar`와 같은 새로운 하위 클래스를 쉽게 추가할 수 있습니다. 이는 코드의 확장성을 크게 향상시킵니다.
- `useVehicle` 함수는 타입 안전성을 유지하면서 다양한 `Vehicle` 타입을 처리할 수 있습니다.

## 핵심 요약
- 상속 구조는 태그 기반 클래스보다 코드의 확장성과 가독성을 높입니다.
- 다형성 활용으로 다양한 클래스를 일관된 방식으로 관리할 수 있습니다.
- 새로운 타입 추가가 용이해 유지보수성이 향상됩니다.