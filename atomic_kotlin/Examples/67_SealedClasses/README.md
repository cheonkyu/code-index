# 67. SealedClasses: 봉인 클래스를 활용한 클래스 계층 제어하기

안녕하세요! 코틀린 프로그래밍을 배우는 여러분, 오늘은 `sealed classes`에 대해 알아보겠습니다. 봉인 클래스는 코드의 안정성과 유지보수성을 크게 향상시키는 강력한 도구입니다. 함께 배워볼까요?

## 기본 개념 이해하기

### 봉인 클래스란?
봉인 클래스(`sealed class`)는 하위 클래스를 특정 파일 내에서만 정의할 수 있도록 하는 코틀린의 특수 클래스 타입입니다. 이를 통해 코드의 예측 가능성과 안전성을 높일 수 있습니다. 특히, 여러 하위 타입 중에서 특정 동작을 처리할 때 유용합니다.

### 예제 코드 살펴보기

#### 1. **비봉인 클래스 예제 (`UnSealed.kt`)**

```kotlin
package withoutsealedclasses
import atomictest.eq // 테스트 라이브러리 가정

// 부모 클래스로 `open class`를 사용했습니다.
open class Transport {
    // 하위 클래스들을 정의합니다.
    data class Train(val line: String) : Transport()
    data class Bus(val number: String, val capacity: Int) : Transport()
}

fun travel(transport: Transport) {
    when (transport) {
        is Train -> "Train ${transport.line}"
        is Bus -> "Bus ${transport.number}: size ${transport.capacity}"
        else -> "$transport is in limbo!" // 하위 클래스가 추가되면 여기에 영향을 줄 수 있음
    }
}

fun main() {
    listOf(Train("S1"), Bus("11", 90))
        .map(::travel) eq "[Train S1, Bus 11: size 90]"
}
```

**해설:**
- 여기서 `Transport` 클래스는 `open class`로 선언되어 하위 클래스를 추가할 수 있습니다.
- `travel` 함수는 `when` 문을 사용해 `Train`과 `Bus` 타입을 구분하지만, 추가적인 하위 클래스(예: `Tram`)가 생기면 `else` 분기가 필요할 수 있습니다.
- 이로 인해 유지보수가 복잡해질 수 있습니다.

#### 2. **봉인 클래스 예제 (`SealedClasses.kt`)**

```kotlin
package sealedclasses
import atomictest.eq // 테스트 라이브러리 가정

// 봉인 클래스로 변경하여 하위 클래스의 범위를 제한합니다.
sealed class Transport {
    data class Train(val line: String) : Transport()
    data class Bus(val number: String, val capacity: Int) : Transport()
}

fun travel(transport: Transport) {
    when (transport) {
        is Train -> "Train ${transport.line}"
        is Bus -> "Bus ${transport.number}: size ${transport.capacity}"
        // else가 필요 없음! 모든 하위 타입이 여기에 포함되어 있으므로
    }
}

fun main() {
    listOf(Train("S1"), Bus("11", 90))
        .map(::travel) eq "[Train S1, Bus 11: size 90]"
}
```

**해설:**
- `Transport` 클래스를 `sealed class`로 변경하여 하위 클래스(`Train`, `Bus`)가 동일한 파일 내에만 정의되도록 했습니다.
- `when` 문에서 `else` 분기가 필요하지 않으므로 코드가 더 간결하고 안전해집니다.
- 새로운 하위 클래스(`Tram`)를 추가하려면 해당 파일 내에서 정의해야 하며, 그렇지 않으면 컴파일 오류가 발생합니다.

## 핵심 개념 요약

1. **봉인 클래스의 목적:**
   - 하위 클래스를 특정 파일 내에서만 정의하도록 제한하여 코드의 안전성을 높입니다.
   - 모든 가능한 타입을 `when` 문에서 처리하도록 강제하여 코드의 완전성을 보장합니다.

2. **비봉인 클래스의 단점:**
   - 새로운 하위 클래스가 추가될 때마다 코드를 수정해야 할 가능성이 있어 유지보수가 어려울 수 있습니다.

3. **사용 시 주의사항:**
   - 봉인 클래스는 하위 타입이 명확하게 정의되어야 하는 상황에 적합합니다.
   - 과도한 다운캐스팅은 피하고, 가능한 경우 다형성을 활용하는 것이 좋습니다.

이렇게 봉인 클래스를 활용하면 코드의 안정성과 유지보수성을 크게 향상시킬 수 있습니다. 코틀린 프로그래밍에서 `sealed classes`는 꼭 익혀야 할 중요한 개념 중 하나입니다! 궁금한 점이 있으면 언제든지 물어보세요!