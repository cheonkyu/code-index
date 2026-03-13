# 55. 인터페이스 (Interfaces)

안녕하세요! 코틀린 프로그래밍을 처음 접하시는 분들을 위해 인터페이스에 대해 친근하게 설명해드릴게요. 인터페이스는 코틀린 프로그래밍에서 중요한 개념 중 하나예요. 이해하기 쉽게 단계별로 설명해볼게요!

## 인터페이스란 무엇인가요?

**인터페이스**는 특정 타입의 개념을 설명하는 거예요. 쉽게 말해, 인터페이스는 어떤 클래스가 가져야 할 기능 목록을 정의하는 거죠. 인터페이스는 무엇을 **해야 하는지** 알려주지만, **어떻게 해야 하는지**는 구체적으로 설명하지 않아요. 즉, 인터페이스는 클래스가 수행해야 할 행동 패턴을 제시하는 역할을 해요.

### 핵심 개념 요약
- **정의**: 클래스가 가져야 할 기능 목록을 정의합니다.
- **목적**: 클래스가 어떤 행동을 해야 하는지 알려주지만, 구체적인 구현 방법은 제공하지 않습니다.
- **예시**: `Computer` 인터페이스는 모든 컴퓨터 관련 클래스가 `prompt()`와 `calculateAnswer()`라는 두 가지 메소드를 구현하도록 요구합니다.

## 인터페이스 사용 예시

### 인터페이스 정의하기
코틀린에서 인터페이스를 정의하려면 `interface` 키워드를 사용해요. 아래는 `Computer` 인터페이스의 예시예요:

```kotlin
// Interfaces/Computer.kt
package interfaces

import atomictest.*

interface Computer {
    fun prompt(): String  // 메시지 출력 메소드
    fun calculateAnswer(): Int  // 계산 결과 반환 메소드
}
```

### 인터페이스 구현하기
인터페이스를 구현하는 클래스는 인터페이스에 정의된 모든 메소드를 구현해야 해요. 아래는 `Computer` 인터페이스를 구현한 `Desktop`, `DeepThought`, `Quantum` 클래스의 예시예요:

```kotlin
class Desktop : Computer {
    override fun prompt(): String = "Hello!"  // 메시지 출력
    override fun calculateAnswer(): Int = 11  // 계산 결과 반환
}

class DeepThought : Computer {
    override fun prompt(): String = "Thinking..."  // 메시지 출력
    override fun calculateAnswer(): Int = 42  // 계산 결과 반환
}

class Quantum : Computer {
    override fun prompt(): String = "Probably..."  // 메시지 출력
    override fun calculateAnswer(): Int = -1  // 계산 결과 반환
}
```

#### `override` 키워드의 중요성
인터페이스 메소드를 구현할 때는 `override` 키워드를 반드시 사용해야 해요. 이 키워드는 해당 메소드가 기존 클래스나 인터페이스 메소드를 재정의한다는 것을 알려주는 역할을 해요:

```kotlin
override fun prompt(): String = "새로운 메시지"  // 인터페이스의 prompt() 메소드 재정의
```

### 인터페이스의 프로퍼티 예시
인터페이스는 프로퍼티도 정의할 수 있어요. 모든 구현 클래스는 이 프로퍼티를 구현해야 합니다:

```kotlin
// Interfaces/PlayerInterface.kt
package interfaces

import atomictest.eq

interface Player {
    val symbol: Char  // 기호 프로퍼티
}

class Food : Player {
    override val symbol: Char = '.'  // 직접 값 지정
}

class Robot : Player {
    override val symbol: Char get() = 'R'  // 커스텀 겟터 사용
}

class Wall(override val symbol: Char) : Player  // 생성자로 프로퍼리 설정
```

#### 메인 함수 예시
다음은 인터페이스 구현 클래스들의 동작을 보여주는 메인 함수 예시예요:

```kotlin
fun main() {
    val computers = listOf(
        Desktop(), DeepThought(), Quantum()
    )
    
    // calculateAnswer 메소드 호출 결과 출력
    computers.map { it.calculateAnswer() }.eq("[11, 42, -1]")
    
    // prompt 메소드 호출 결과 출력
    computers.map { it.prompt() }.eq("[Hello!, Thinking..., Probably...]")
}
```

### 열거형과 인터페이스
인터페이스는 열거형과도 잘 어울립니다. 아래는 `SpiceLevel` 열거형이 `Hotness` 인터페이스를 구현한 예시예요:

```kotlin
// Interfaces/Hotness.kt
package interfaces

import atomictest.*

interface Hotness {
    fun feedback(): String  // 피드백 메소드
}

enum class SpiceLevel : Hotness {
    Mild {
        override fun feedback() = "It adds flavor!"
    },
    Medium {
        override fun feedback() = "Is it warm in here?"
    },
    Hot {
        override fun feedback() = "I'm suddenly sweating a lot."
    },
    Flaming {
        override fun feedback() = "I'm in pain. I am suffering."
    }
}

fun main() {
    SpiceLevel.values().map { it.feedback() }.eq(
        "[It adds flavor!, Is it warm in here?, I'm suddenly sweating a lot., I'm in pain. I am suffering.]"
    )
}
```

### 요약
- **인터페이스**는 클래스가 가져야 할 행동 패턴을 정의합니다.
- **구현 클래스**는 인터페이스에 정의된 모든 메소드를 구현해야 합니다.
- **`override`** 키워드는 메소드 재정의를 명시합니다.
- **프로퍼티**도 인터페이스를 통해 정의하고 구현 클래스에서 재정의할 수 있어요.
- **열거형**도 인터페이스를 구현할 수 있어 다양한 상황에서 활용 가능합니다.

이렇게 인터페이스를 이해하고 활용하면 코드의 유연성과 재사용성이 크게 향상되어요. 코틀린 프로그래밍을 더욱 즐겁게 배워보세요! 궁금한 점이 있으면 언제든지 물어봐 주세요. 😊