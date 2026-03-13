# 42. 확장 속성 (Extension Properties)

안녕하세요! 코틀린 프로그래밍을 처음 배우는 분들을 위해 이번 챕터에서는 **확장 속성 (Extension Properties)**에 대해 친근하게 설명해드릴게요. 확장 속성이란 기존 클래스에 새로운 속성을 추가하는 방법으로, 코드를 더 간결하고 읽기 쉽게 만드는 데 도움이 됩니다. 함께 알아볼게요!

## 기본 개념 이해하기

### 확장 속성의 문법
확장 속성을 정의할 때는 기존 타입 바로 뒤에 속성 이름을 붙이는 방식을 사용해요. 예를 들어:

```kotlin
// 확장 속성 정의 예시: String 클래스에 indices 속성 추가
package extensionproperties

import atomictest.eq

// 확장 속성 정의
val String.indices: IntRange
    get() = this.indices // 각 문자열에 대해 인덱스 범위 반환

fun main() {
    "abc".indices eq 0..2 // "abc"의 인덱스 범위가 0부터 2까지인지 확인
}
```

#### 핵심 포인트
- **수신 타입 (Receiver Type)**: 확장 속성을 정의할 때 확장 대상 타입이 속성 앞에 옵니다 (`String` 같은 경우).
- **Getter 필요성**: 확장 속성은 반드시 커스텀 getter를 필요로 합니다. 각 접근 시 속성 값을 새로 계산해요.

## 실용적인 예제 살펴보기

### 제네릭 확장 속성 예제
기존 제네릭 함수를 확장 속성으로 변환해보겠습니다. 예를 들어, `firstOrNull()`을 확장 속성으로 만들어볼게요:

```kotlin
// 제네릭 확장 속성 예시: List<T>에 firstOrNull 속성 추가
package extensionproperties

import atomictest.eq

// 제네릭 확장 속성 정의
val <T> List<T>.firstOrNull: T?
    get() = if (isEmpty()) null else this[0] // 리스트가 비어있으면 null 반환, 아니면 첫 번째 요소 반환

fun main() {
    listOf(1, 2, 3).firstOrNull eq 1 // 정수 리스트의 첫 번째 요소가 1인지 확인
    listOf<String>().firstOrNull eq null // 빈 문자열 리스트의 경우 null 반환 확인
}
```

### 타입 정보 손실 주의사항
제네릭 확장 속성에서 `*`를 사용할 때 주의해야 할 점이 있어요:

```kotlin
// 타입 정보가 손실되는 예제
package extensionproperties

import atomictest.eq

// List<*> 사용 시 타입 정보 손실
val List<*>.indices: IntRange
    get() = 0 until size // 리스트의 인덱스 범위 반환

fun main() {
    listOf(1).indices eq 0..0 // 숫자 리스트의 인덱스 확인
    listOf('a', 'b', 'c', 'd').indices eq 0..3 // 문자 리스트의 인덱스 확인
    emptyList<Int>().indices eq IntRange.EMPTY // 빈 리스트의 경우 빈 범위 확인
}
```

**주의**: `List<*>`를 사용하면 타입 정보가 사라지므로, 반환 값은 `Any?` 타입으로 제한됩니다. 예를 들어, 리스트의 첫 번째 요소를 가져올 때 `Any?` 타입으로 취급해야 해요:

```kotlin
import atomictest.eq

fun main() {
    val list: List<*> = listOf(1, 2)
    val any: Any? = list[0] // 리스트의 첫 번째 요소를 Any? 타입으로 처리
    any eq 1 // 요소가 정수인 경우 확인
}
```

## 핵심 요약
- **확장 속성**은 기존 클래스에 새로운 속성을 추가하여 코드를 더 간결하게 만드는 방법입니다.
- **Getter 필요**: 확장 속성은 항상 커스텀 getter를 가져야 합니다.
- **타입 정보 주의**: 제네릭 확장 속성에서 `*`를 사용하면 타입 정보가 손실될 수 있으므로 주의해야 합니다.
- **실용성 고려**: 확장 속성은 가독성을 향상시키는 데 유용하지만, 함수보다 복잡해지지 않도록 신중하게 선택해야 합니다.

이제 확장 속성에 대해 좀 더 친숙해졌기를 바라요! 연습 문제와 더 자세한 내용은 [AtomicKotlin 공식 웹사이트](www.AtomicKotlin.com)에서 확인해보세요. 함께 공부하다 보면 코틀린 프로그래밍이 훨씬 쉬워질 거예요! 궁금한 점이 있으면 언제든지 물어보세요!