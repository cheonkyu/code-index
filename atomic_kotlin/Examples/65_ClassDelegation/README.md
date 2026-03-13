# 65. ClassDelegation: 클래스 위임으로 코드 재사용하기

안녕하세요, 코틀린 초보자 여러분! 오늘은 코틀린에서 **클래스 위임(Class Delegation)**에 대해 배워볼게요. 이 주제는 상속과 구성(composition) 사이에서 멋진 중간 지점을 제공하며, 코드 재사용성을 크게 높여줍니다. 초보자분들이 이해하기 쉽게 차근차근 설명해볼게요.

## 핵심 개념 요약

- **상속(Inheritance)**: 부모 클래스의 속성과 메소드를 물려받지만, 암시적으로 이루어집니다.
- **구성(Composition)**: 객체를 직접 클래스 내부에 포함시켜 사용하지만, 인터페이스 노출은 제한적입니다.
- **클래스 위임(Class Delegation)**: 구성과 상속의 장점을 결합한 방법으로, 객체의 인터페이스를 노출하면서 필요한 메소드를 위임할 수 있습니다.

### 클래스 위임의 장점

- **재사용성 향상**: 기존 클래스의 구현을 재사용할 수 있습니다.
- **유연성**: 필요한 경우 인터페이스를 노출하고 메소드를 위임하거나 오버라이드할 수 있습니다.
- **간결한 코드**: 명시적으로 함수를 구현하지 않아도 되므로 코드가 더 간결해집니다.

## 예제 설명

### 1. 기본 개념 이해하기

#### 제어 모듈 인터페이스 (`Controls`)

우선, 제어 모듈 인터페이스를 정의해봅시다. 이 인터페이스는 우주선 제어에 필요한 다양한 메소드를 정의합니다.

```kotlin
// Control 인터페이스 정의
package classdelegation

interface Controls {
    fun up(velocity: Int): String
    fun down(velocity: Int): String
    fun left(velocity: Int): String
    fun right(velocity: Int): String
    fun forward(velocity: Int): String
    fun back(velocity: Int): String
    fun turboBoost(): String
}
```

#### 기본 제어 클래스 (`SpaceShipControls`)

이 클래스는 `Controls` 인터페이스를 구현하여 기본 제어 기능을 제공합니다.

```kotlin
// SpaceShipControls 클래스 정의
package classdelegation

class SpaceShipControls : Controls {
    override fun up(velocity: Int) = "up $velocity"
    override fun down(velocity: Int) = "down $velocity"
    override fun left(velocity: Int) = "left $velocity"
    override fun right(velocity: Int) = "right $velocity"
    override fun forward(velocity: Int) = "forward $velocity"
    override fun back(velocity: Int) = "back $velocity"
    override fun turboBoost() = "turbo boost"
}
```

### 2. 명시적 위임 (Explicit Delegation)

기존 클래스의 기능을 재사용하되 인터페이스를 명시적으로 위임하는 방법입니다.

```kotlin
// ExplicitControls 클래스 정의
package classdelegation

import atomictest.eq // 테스트용 라이브러리 가정

class ExplicitControls : Controls {
    private val controls = SpaceShipControls() // 제어 객체 생성

    // 명시적으로 위임하는 메소드들
    override fun up(velocity: Int) = controls.up(velocity)
    override fun down(velocity: Int) = controls.down(velocity)
    override fun left(velocity: Int) = controls.left(velocity)
    override fun right(velocity: Int) = controls.right(velocity)
    override fun forward(velocity: Int) = controls.forward(velocity)
    override fun back(velocity: Int) = controls.back(velocity)
    override fun turboBoost() = controls.turboBoost() + "... boooooost!"
}

// 테스트 코드
fun main() {
    val controls = ExplicitControls()
    println(controls.forward(100) eq "forward 100") // 출력: true
    println(controls.turboBoost() eq "turbo boost... boooooost!") // 출력: true
}
```

### 3. Kotlin의 자동화된 클래스 위임 (by 키워드 사용)

Kotlin은 이 과정을 자동화해줍니다. `by` 키워드를 사용하면 명시적 위임 코드를 간결하게 작성할 수 있습니다.

```kotlin
// Basic Delegation 예시
package classdelegation

interface AI
class A : AI // 인터페이스 구현 클래스
class B(val a: A) : AI by a // B 클래스가 A 인터페이스를 위임

// Explicit Delegation을 간결하게 작성하기
// DelegatedControls 클래스 정의
package classdelegation

import atomictest.eq

class DelegatedControls(
    private val controls: SpaceShipControls = SpaceShipControls() // 위임할 객체 생성
) : Controls by controls { // 인터페이스 위임
    override fun turboBoost(): String = "${controls.turboBoost()}... boooooost!"
}

// 테스트 코드
fun main() {
    val controls = DelegatedControls()
    println(controls.forward(100) eq "forward 100") // 출력: true
    println(controls.turboBoost() eq "turbo boost... boooooost!") // 출력: true
}
```

### 요약

- **클래스 위임**은 상속과 구성의 장점을 결합하여 코드를 더 간결하고 유연하게 만듭니다.
- **`by` 키워드**를 사용하면 명시적 위임 코드를 훨씬 간결하게 작성할 수 있습니다.
- 이를 통해 기존 클래스의 구현을 재사용하면서도 필요한 기능을 오버라이드하거나 확장할 수 있습니다.

이제 코틀린에서 클래스 위임을 활용해보세요! 코드가 더 깔끔해지고 유지보수가 쉬워질 거예요. 질문이 있으면 언제든지 물어보세요! 😊