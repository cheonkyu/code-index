# 58. Inheritance (상속)

상속은 기존 클래스를 재사용하고 수정하여 새로운 클래스를 만드는 메커니즘입니다. 쉽게 말해, 이미 잘 작동하는 클래스를 기반으로 좀 더 특화된 클래스를 만드는 방법이죠. 이렇게 하면 코드를 효율적으로 재사용할 수 있고, 필요한 기능만 추가하거나 변경할 수 있어요.

## 기본 개념 이해하기

### 클래스와 객체
- **클래스**는 객체의 설계도나 템플릿 같은 거예요. 클래스는 속성(데이터)과 함수(동작)를 정의합니다.
- **객체**는 클래스를 기반으로 생성된 개별 인스턴스입니다. 각 객체는 독립적인 데이터를 가질 수 있어요.

### 상속의 필요성
기존 클래스를 그대로 사용하면서 일부 수정이나 추가 기능을 원할 때 상속을 사용합니다. 새로운 클래스를 처음부터 만드는 것보다 훨씬 효율적이죠!

## 상속의 구문
Kotlin에서 상속을 구현하는 방법은 간단해요:

```kotlin
// 패키지 선언
package inheritance

// 기본 클래스 정의
open class Base {
    // 기본 클래스의 속성과 함수 정의
    fun printBaseInfo() {
        println("이것은 Base 클래스입니다.")
    }
}

// 파생 클래스 정의 (기본 클래스 Base를 상속)
class Derived : Base() {
    // 기본 클래스의 함수를 오버라이드하거나 추가 함수를 정의할 수 있어요.
    override fun printBaseInfo() {
        super.printBaseInfo() // 부모 클래스의 함수 호출
        println("그리고 여기에는 Derived 클래스의 추가 정보가 들어갑니다.")
    }
}
```

### 핵심 용어
- **기본 클래스 (Base Class)**: 상속을 받는 클래스입니다. `open` 키워드로 선언되어야 합니다.
- **파생 클래스 (Derived Class)**: 기본 클래스를 상속받는 클래스입니다.
- **부모 클래스 (Super Class)**: 상속을 제공하는 클래스입니다.
- **자식 클래스 (Sub Class)**: 상속을 받는 클래스입니다.

## 오픈 클래스와 최종 클래스
Kotlin에서는 기본적으로 모든 클래스가 `final`로 설정되어 있어요. 하지만 상속을 원할 때는 `open` 키워드를 사용해야 합니다:

```kotlin
// 상속 가능한 클래스 (기본 클래스)
open class Parent {
    // 상속 가능한 속성과 함수
}

// 상속 불가능한 클래스 (최종 클래스)
final class Single {
    // 상속 불가능
}
```

### 예제 설명
위 예제에서 `GreatApe` 클래스는 기본 클래스 역할을 합니다:

```kotlin
package inheritance.ape1
import atomictest.eq

// 기본 클래스 정의 (상속 가능하도록 open 키워드 사용)
open class GreatApe {
    val weight = 100.0
    val age = 12

    // 모든 파생 클래스에서 공유할 함수 정의
    fun info() = "wt: $weight age: $age"
}

// 파생 클래스들
open class Bonobo : GreatApe()  // GreatApe를 상속
class Chimpanzee : GreatApe() // GreatApe를 상속
class BonoboB : Bonobo()       // Bonobo를 상속

fun GreatApe.info() = "wt: $weight age: $age"  // 확장 함수

fun main() {
    // 모든 파생 클래스에서 `info` 함수가 동일하게 작동
    println(GreatApe().info())  // "wt: 100.0 age: 12"
    println(Bonobo().info())    // "wt: 100.0 age: 12"
    println(Chimpanzee().info()) // "wt: 100.0 age: 12"
    println(BonoboB().info())   // "wt: 100.0 age: 12"
}
```

### 주요 핵심 개념 요약
1. **상속을 통해 코드 재사용**: 기존 클래스의 속성과 함수를 활용하여 새로운 클래스를 만듭니다.
2. **`open` 키워드**: 상속을 허용하기 위해 기본 클래스에 사용합니다.
3. **확장 함수**: 파생 클래스에서 부모 클래스의 함수를 오버라이드하거나 추가할 수 있어요.
4. **동일한 기능 공유**: 상속 관계에 있는 모든 클래스에서 공통 함수를 쉽게 공유하고 사용할 수 있어요.

이렇게 상속을 활용하면 코드를 간결하게 유지하면서도 다양한 클래스를 효과적으로 관리할 수 있답니다. 상속을 배우면서 더 복잡한 프로그램을 만들어 보세요!