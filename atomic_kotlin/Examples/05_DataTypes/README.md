# 05. 데이터 타입 (Data Types)

안녕하세요! Kotlin 프로그래밍을 처음 시작하시는 분들을 위해 데이터 타입에 대해 쉽게 설명해드릴게요. 데이터 타입이란 무엇인지부터 알아보면서 함께 배워보도록 하죠.

## 데이터 타입이란 무엇인가요?

컴퓨터는 데이터를 다루는데 있어서 여러 가지 종류의 형태를 인식하고 처리해야 해요. 예를 들어 수학 문제를 풀 때처럼 `5.9 + 6` 이라는 표현을 쓰면, 우리는 결과가 어떤 종류의 숫자인지 알죠 — 여기서는 소수점이 있는 숫자, 즉 `Double` 타입과 정수, 즉 `Int` 타입을 사용하게 됩니다. Kotlin도 이런 정보를 알고 있어요!

### Kotlin의 타입 이해하기

- **Double (소수점 숫자)**: `5.9` 와 같은 숫자는 Kotlin에서 `Double` 타입으로 인식해요.
- **Int (정수)**: `6` 과 같은 숫자는 `Int` 타입으로 인식해요.

**타입의 역할**:
- **데이터 사용 방법 지시**: 어떤 방식으로 데이터를 사용할지 알려줘요.
- **연산 규칙 정의**: 어떤 연산을 수행할 수 있는지 정의해요.
- **데이터 저장 방법**: 데이터를 어떻게 저장할지 결정해요.

Kotlin은 이러한 타입을 통해 코드의 정확성을 검사해요. 예를 들어, `5.9 + 6` 과 같은 표현에서는 결과가 `Double` 타입으로 자동으로 처리되죠. 만약 타입 규칙을 위반하면 오류 메시지를 보여줘요.

### 타입 예시: 문자열과 숫자 더하기

#### 예제 코드: `StringPlusNumber.kt`

```kotlin
fun main() {
    println("Sally" + 5.9)  // 오류가 발생하지 않고 문자열이 붙어 출력됨
}
/* 출력 결과:
Sally5.9
*/
```

이 코드에서 Kotlin은 문자열과 숫자를 붙이는 것을 문자열 연결로 해석해요. 하지만 잘못된 타입 조합은 오류를 일으키죠.

#### 예제 코드: 잘못된 타입 조합

```kotlin
fun main() {
    println("Sally" * 5.9)  // 오류 발생: 타입 규칙 위반
}
/* 오류 메시지:
Error:(8, 29): Type mismatch: Cannot implicitly convert expression of type Double to String.
*/
```

문자열과 숫자를 곱하는 것은 의미가 없으므로 오류가 발생해요.

### 타입 추론 (Type Inference)

Kotlin은 코드를 간결하게 작성할 수 있도록 타입을 자동으로 추론해요. 예를 들어:

#### 타입 추론 예제: `Inference.kt`

```kotlin
fun main() {
    val n = 1 + 1.2  // Int와 Double을 더함
    println(n)       // 결과는 Double 타입으로 출력됨
}
/* 출력 결과:
2.2
*/
```

여기서 `1`은 `Int` 타입이고 `1.2`는 `Double` 타입이지만, Kotlin은 결과를 `Double` 타입으로 자동으로 결정해요.

## Kotlin의 기본 타입들

Kotlin에서 자주 사용되는 기본 타입들을 알아볼게요:

- **Int**: 정수형 숫자 (예: `val whole: Int = 11`)
- **Double**: 소수점 숫자 (예: `val fractional: Double = 1.4`)
- **Boolean**: 참/거짓 (예: `val trueOrFalse: Boolean = true`)
- **String**: 문자열 (예: `val words: String = "A value"`)
- **Char**: 문자 하나 (예: `val character: Char = 'z'`)
- **멀티라인 문자열**: `""" """` (예: `val lines: String = """Triple quotes let\nyou have many lines\nin your string"""`)

#### 예제 코드: 기본 타입 사용

```kotlin
fun main() {
    val whole: Int = 11          // 정수형 변수
    val fractional: Double = 1.4 // 소수점 숫자 변수
    val trueOrFalse: Boolean = true  // 불리언 변수
    val words: String = "A value"  // 문자열 변수
    val character: Char = 'z'     // 문자 변수
    val lines: String = """Triple quotes let
                            |you have many lines
                            |in your string""".trimMargin() // 멀티라인 문자열

    println(whole)
    println(fractional)
    println(trueOrFalse)
    println(words)
    println(character)
    println(lines)
}
/* 출력 결과:
11
1.4
true
A value
z
Triple quotes let
you have many lines
in your string
*/
```

### 요약
- **타입은 데이터의 종류와 사용법을 정의합니다**: Kotlin은 이를 통해 코드의 안정성을 높여줘요.
- **타입 추론**: 명시적으로 타입을 지정하지 않아도 Kotlin이 자동으로 타입을 결정해요.
- **기본 타입들**: Kotlin에서 자주 사용되는 기본 타입들을 이해하고 활용하면 코드를 더 명확하게 작성할 수 있어요.

### 연습해보기
더 많은 예제와 연습 문제는 [Atomic Kotlin 공식 웹사이트](www.AtomicKotlin.com)에서 찾아볼 수 있어요. 함께 연습해보면서 더 익숙해져봐요!

이제 Kotlin의 데이터 타입에 대해 조금 더 자신감을 가지고 코딩해보세요. 질문 있으시면 언제든지 물어봐 주세요! 😉