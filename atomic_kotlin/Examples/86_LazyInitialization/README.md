# 86. LazyInitialization: 지연 초기화로 효율적인 코드 작성하기

안녕하세요! 코틀린 프로그래밍을 배우고 계신 여러분께 조금 더 친절하게 설명해드리려고 합니다. 이번 챕터에서는 **지연 초기화 (Lazy Initialization)**에 대해 배워볼게요. 지연 초기화는 특히 비용이 많이 드는 작업 (예: 복잡한 계산, 네트워크 요청, 데이터베이스 접근 등)을 필요할 때만 실행하도록 하는 방법이에요. 이 방법을 통해 애플리케이션의 시작 시간을 단축하고, 불필요한 작업을 피할 수 있어요. 그럼 초보자분들이 이해하기 쉽게 핵심 내용을 풀어보도록 할게요!

## 핵심 개념 요약

### 1. 지연 초기화의 필요성
- **비용이 많이 드는 작업**: 복잡한 계산이나 네트워크 요청은 실행 시점에 따라 필요성이 달라질 수 있어요. 이런 작업을 처음부터 실행하면 애플리케이션의 시작 시간이 길어질 수 있죠.
- **불필요한 작업 방지**: 만약 해당 속성을 전혀 사용하지 않거나 나중에 사용할 경우에도 초기화를 지연시키면 효율적이에요.

### 2. 코틀린에서의 지연 초기화 방법
코틀린은 `lazy` 키워드를 이용해 지연 초기화를 쉽게 구현할 수 있게 해줍니다. 기본 구조는 다음과 같아요:
```kotlin
val lazyProperty by lazy { initializer }
```
여기서 `initializer`는 초기화 로직을 담은 람다 표현식입니다.

### 예제 코드로 이해해보기

#### 간단한 지연 초기화 예시
```kotlin
package lazyinitialization

import atomictest.*

// 지연 초기화를 사용한 예시
val idle: String by lazy {
    trace("초기화 중: 'idle'")
    "이 사용되지 않아요"
}

val helpful: String by lazy {
    trace("초기화 중: 'helpful'")
    "도움이 되고 있어요!"
}

fun main() {
    trace(helpful)  // "도움이 되고 있어요!"만 출력
    // idle은 아무 작업도 수행하지 않아요 (사용되지 않아서 초기화되지 않음)
}
```
**설명**:
- `idle`은 절대 사용되지 않으므로 초기화되지 않아요.
- `helpful`은 처음 호출될 때만 초기화되고, 그 이후에는 바로 값이 반환되요.

#### 기본적인 지연 초기화 구현 방식 비교
지연 초기화와 다른 초기화 방법들을 비교해볼게요:
```kotlin
package lazyinitialization

import atomictest.trace

fun compute(i: Int): Int {
    trace("계산 중: $i")
    return i
}

object Properties {
    // 정의 시점 초기화
    val atDefinition = compute(1)
    
    // 매번 접근 시 초기화
    val getter: String
    get() = compute(2)
    
    // 지연 초기화
    val lazyInit by lazy { compute(3) }
    
    // 절대 사용되지 않는 지연 초기화 예시
    val never by lazy { compute(4) }
}

fun main() {
    listOf(
        Properties::atDefinition,
        Properties::getter,
        Properties::lazyInit
    ).forEach { prop ->
        trace("${it.name}:")
        trace(it.get())  // 각 초기화 시점 출력
        trace(it.get())  // 동일한 결과를 다시 확인
    }
}
```
**설명**:
- `atDefinition`은 클래스 생성 시 바로 계산됩니다.
- `getter`는 각 접근 시마다 계산됩니다.
- `lazyInit`은 처음 접근 시에만 계산되고 이후에는 저장된 값을 사용합니다.
- `never`는 절대 사용되지 않으므로 초기화 작업이 아예 이루어지지 않습니다.

## 요약
지연 초기화는 애플리케이션의 효율성을 크게 향상시켜줍니다. 특히 비용이 많이 드는 작업을 필요할 때만 실행하도록 해서 시작 시간을 단축하고 불필요한 작업을 피할 수 있어요. 코틀린의 `lazy` 키워드를 활용하면 코드를 간결하고 읽기 쉽게 작성할 수 있습니다.

이제 연습 문제들을 풀어보면서 직접 지연 초기화를 적용해보는 건 어떨까요? 자세한 연습 문제와 해답은 [AtomicKotlin 웹사이트](www.AtomicKotlin.com)에서 확인할 수 있어요!

궁금한 점이 있으면 언제든지 물어봐주세요. 함께 배워나가는 즐거움이 있으니까요! 😊