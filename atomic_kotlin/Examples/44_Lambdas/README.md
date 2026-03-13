# 44. Lambdas (람다)

안녕하세요! 코틀린 프로그래밍을 처음 접하는 분들을 위해 람다(Lambda)에 대해 쉽게 설명해 드릴게요. 람다는 코드를 간결하고 이해하기 쉽게 만드는 멋진 도구랍니다. 함께 배워볼까요?

## 무엇이 람다인가요?

람다는 **함수 리터럴**이라고도 부르며, 이름이 없는 간단한 함수입니다. 주요 특징은 다음과 같아요:
- **이름 없음**: 직접 이름을 부여하지 않아도 됩니다.
- **간결함**: 최소한의 코드로 생성 가능합니다.
- **직접 삽입**: 다른 코드 안에 바로 삽입할 수 있어요.

### 기본 예제: `map()` 함수

`map()` 함수는 리스트 같은 컬렉션에 대해 각 요소에 함수를 적용하고 새로운 리스트를 반환해요. 예를 들어, 정수 리스트의 각 요소를 문자열로 변환해 보죠.

```kotlin
import atomictest.eq

fun main() {
    // 정수 리스트 생성
    val list = listOf(1, 2, 3, 4)
    
    // 람다를 사용해 각 요소를 "[숫자]" 형태로 변환
    val result = list.map({ n: Int -> "[$n]" })
    
    // 결과 검증
    result eq listOf("[1]", "[2]", "[3]", "[4]")
}
```

#### 핵심 포인트 요약:
- **람다 정의**: `{ 매개변수 -> 표현식 }` 형태로 작성합니다.
- **매개변수와 화살표**: `매개변수`는 화살표(`->`)로 구분하고, `표현식`이 결과를 반환합니다.
- **타입 추론**: Kotlin은 주변 컨텍스트를 통해 타입을 자동으로 추론할 수 있어요. 예를 들어, `n`의 타입은 `Int`로 자동으로 결정됩니다.

```kotlin
// 타입 추론 예시
fun main() {
    val list = listOf(1, 2, 3, 4)
    val result = list.map({ n -> "[$n]" })  // 타입 명시 없이 사용 가능
    result eq listOf("[1]", "[2]", "[3]", "[4]")
}
```

## 람다 간단화

람다를 더 간결하게 작성할 수 있어요. 특히 단일 매개변수일 때는 이름을 자동으로 생성해 줍니다.

```kotlin
// 단일 매개변수 람다 예시
fun main() {
    val list = listOf(1, 2, 3, 4)
    val result = list.map({ "[$it]" })  // `it`을 사용해 타입 추론
    result eq listOf("[1]", "[2]", "[3]", "[4]")
}
```

## 다양한 람다 사용법

### 리스트의 요소를 다른 형식으로 변환 (`joinToString`)

```kotlin
// 여러 매개변수를 가진 람다 예시: joinToString
fun main() {
    val list = listOf('a', 'b', 'c', 'd')
    val result = list.joinToString(" ") { "[${it.toUpperCase()}]" }
    println(result)  // "[A] [B] [C] [D]" 출력
}
```

### 명명된 인수와 람다 함께 사용

```kotlin
// 명명된 인수와 람다 함께 사용 예시
fun main() {
    val list = listOf(9, 11, 23, 32)
    list.joinToString(
        separator = " ",  // 구분자
        transform = { "[$it]" }  // 람다로 변환
    ) eq "[9] [11] [23] [32]"
}
```

### 여러 매개변수를 가진 람다

```kotlin
// 여러 매개변수 람다 예시: mapIndexed
fun main() {
    val list = listOf('a', 'b', 'c')
    val result = list.mapIndexed { index, element -> "[$index: $element]" }
    result eq listOf("[0: a]", "[1: b]", "[2: c]")
}
```

### 사용하지 않는 매개변수 무시

```kotlin
// 사용하지 않는 매개변수 무시 예시
fun main() {
    val list = listOf('a', 'b', 'c')
    val result = list.map { _, element -> "[$element]" }  // 첫 번째 매개변수 `_` 사용
    result eq listOf("[a]", "[b]", "[c]")
}
```

## 요약
- **람다는 간결한 함수**: 이름 없이 코드 블록을 직접 삽입 가능합니다.
- **타입 추론**: Kotlin은 주변 컨텍스트를 통해 타입을 자동으로 추론합니다.
- **다양한 활용**: `map()`, `joinToString()`, `mapIndexed()` 등 다양한 함수와 함께 사용 가능합니다.

이제 코틀린 람다에 대해 좀 더 친숙하게 느끼셨길 바랍니다! 계속 연습하면 점점 더 자연스럽게 사용할 수 있을 거예요. 화이팅!