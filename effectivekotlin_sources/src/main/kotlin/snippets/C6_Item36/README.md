# Item 36: 상속 대신 구성 사용하기

## 핵심 가이드라인 및 이유

상속을 선호하는 대신, **구성(Composition)**을 사용하는 것이 훨씬 더 안전하고 유연한 접근 방식입니다. 상속은 클래스 간의 깊은 의존성을 초래할 수 있으며, 이로 인해 변경이나 확장이 복잡해질 수 있습니다. 반면에 구성은 객체 간의 관계를 더 유연하게 설계할 수 있게 해줍니다. 구성을 통해 다양한 역할이나 기능을 가진 객체들을 쉽게 교체하거나 조합할 수 있어, 시스템의 유지보수와 확장성을 크게 향상시킵니다.

### 상속의 문제점
- **깊은 상속 계층**: 상속을 지나치게 사용하면 복잡한 상속 계층이 생겨 코드 이해와 유지보수에 어려움이 생깁니다.
- **결합도 높음**: 하위 클래스가 상위 클래스의 내부 구현에 크게 의존하게 되어 변경 시 부작용이 발생할 가능성이 높아집니다.
- **유연성 부족**: 특정 기능이 변경되거나 확장될 때, 전체 클래스 구조를 수정해야 할 수 있습니다.

### 구성의 장점
- **유연성**: 구성을 통해 객체 간의 상호작용을 더 자유롭게 설계할 수 있습니다. 필요한 기능을 가진 객체를 외부에서 쉽게 교체하거나 추가할 수 있습니다.
- **결합도 낮음**: 객체 간의 의존성이 줄어들어 변경에 대한 영향이 최소화됩니다.
- **확장성**: 새로운 기능을 추가하거나 기존 기능을 수정할 때 시스템 전체에 미치는 영향을 최소화할 수 있습니다.

## 예제 코드

아래는 상속 대신 구성을 사용한 예제입니다. `Car` 클래스가 `Engine`과 `Wheel` 컴포넌트를 가질 때 구성 방식으로 구현한 예시입니다.

```kotlin
// 상속 방식 예시 (비교를 위한)
abstract class Vehicle {
    open fun start() {
        println("차량 시작")
    }
}

class Car : Vehicle() {
    override fun start() {
        println("스포츠카 시작")
    }
    abstract class Engine {
        open fun start() {
            println("엔진 시작")
        }
    }
    class ElectricEngine : Engine() {
        override fun start() {
            println("전기 엔진 시작")
        }
    }
    val engine: Engine = ElectricEngine()

    fun drive() {
        engine.start()
        println("달리기")
    }
}

// 구성 방식 예시
class Car {
    private val engine: Engine = ElectricEngine()
    private val wheels: List<Wheel> = listOf(Wheel(), Wheel(), Wheel(), Wheel())

    fun start() {
        engine.start()
        println("달리기")
    }

    fun changeEngine(newEngine: Engine) {
        engine = newEngine
    }

    fun addWheel(wheel: Wheel) {
        wheels += wheel
    }
}

// 컴포넌트 클래스 예시
class Engine {
    fun start() {
        println("엔진 시작")
    }
}

class ElectricEngine : Engine() {
    override fun start() {
        println("전기 엔진 시작")
    }
}

class Wheel {}

fun main() {
    val myCar = Car()
    myCar.start()  // 출력: 엔진 시작, 달리기

    // 엔진 교체 예시
    val newEngine = ElectricEngine()
    myCar.changeEngine(newEngine)
    myCar.start()  // 출력: 전기 엔진 시작, 달리기

    // 휠 추가 예시
    myCar.addWheel(Wheel())
    println("휠 개수: ${myCar.wheels.size}")  // 출력: 휠 개수: 5
}
```

## 핵심 요약
- **구성 사용**: 상속 대신 객체 간의 유연한 관계를 구축하여 코드의 유연성과 유지보수성을 높입니다.
- **교체와 확장 용이**: 필요한 컴포넌트를 쉽게 교체하거나 추가할 수 있어 시스템의 확장성이 향상됩니다.
- **결합도 감소**: 구성은 객체 간의 의존성을 줄여 변경 시 부작용을 최소화합니다.