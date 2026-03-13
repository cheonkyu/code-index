# 09. Number Types

안녕하세요! 오늘은 Kotlin에서 숫자 타입에 대해 알아볼게요. 처음 접하는 분들도 쉽게 이해할 수 있도록 친절하게 설명해볼게요.

## 기본 숫자 타입과 추론

Kotlin에서는 다양한 숫자 타입이 서로 다른 방식으로 저장됩니다. 만약 정수 값을 변수에 할당하면, Kotlin은 자동으로 그 변수를 `Int` 타입으로 인식해요. 예를 들어, 아래 코드를 보세요:

```kotlin
fun main() {
    val million = 1_000_000 // 밑줄(_)을 사용하여 숫자를 더 읽기 쉽게 작성할 수 있어요
    println(million) // 출력: 1000000
}
```

**핵심 개념:**
- `Int` 타입은 정수를 저장하는데 사용됩니다.
- 밑줄(_)은 숫자 사이에 넣어 가독성을 높여줍니다.

## 기본 수학 연산자

Kotlin에서 숫자 연산은 대부분의 프로그래밍 언어와 비슷해요. 주요 연산자는 다음과 같습니다:

- **덧셈 (+)**
- **뺄셈 (-)**
- **나눗셈 (/)**
- **곱셈 (*)**
- **나머지 연산자 (%)**: 정수 나눗셈의 나머지를 반환합니다.

### 나머지 연산자 예시

```kotlin
fun main() {
    val numerator: Int = 19
    val denominator: Int = 10
    println(numerator % denominator) // 출력: 9
}
```

**핵심 개념:**
- 나눗셈 연산자 `/`는 결과를 잘라냅니다 (정수 나눗셈 결과는 소수점 아래를 버리죠).

### 정수 나눗셈의 특성

정수 나눗셈은 결과를 잘라내므로 주의가 필요해요:

```kotlin
fun main() {
    val numerator: Int = 19
    val denominator: Int = 10
    println(numerator / denominator) // 출력: 1
    // 만약 결과가 반올림되었다면 출력은 2가 되었을 것입니다.
}
```

**핵심 개념:**
- 정수 나눗셈 결과는 소수점 아래를 잘라내기 때문에 정확한 결과를 얻기 어렵습니다.

## 연산 순서

연산 순서는 기본적인 산술 규칙에 따릅니다:

```kotlin
fun main() {
    println(45 + 5 * 6) // 출력: 75
    // 곱셈이 덧셈보다 먼저 수행됩니다.
}
```

괄호를 사용하면 원하는 순서로 연산할 수 있어요:

```kotlin
fun main() {
    println((45 + 5) * 6) // 출력: 300
    // 괄호 안의 연산이 먼저 수행됩니다.
}
```

**핵심 개념:**
- 연산 순서는 기본적으로 곱셈과 나눗셈이 덧셈과 뺄셈보다 먼저 이루어집니다. 괄호를 사용하여 우선순위를 변경할 수 있습니다.

## 실제 예제: BMI 계산

BMI (체질량지수) 계산은 숫자 타입 선택의 중요성을 잘 보여줍니다. `Double` 타입을 사용하면 더 정확한 결과를 얻을 수 있어요:

### `Double` 타입 사용 예제

```kotlin
fun bmiMetric(
    weight: Double,
    height: Double
): String {
    val bmi = weight / (height * height)
    return if (bmi < 18.5) "Underweight"
    else if (bmi < 25) "Normal weight"
    else "Overweight"
}

fun main() {
    val weight = 72.57 // 파운드 (lb)
    val height = 1.727 // 미터 (m)
    val status = bmiMetric(weight, height)
    println(status) // 출력: Normal weight
}
```

**핵심 개념:**
- `Double` 타입은 소수점을 포함한 더 정밀한 계산이 가능합니다.

### 정수 타입 사용 시 주의사항

정수 타입을 사용하면 정확도가 떨어질 수 있어요:

```kotlin
fun bmiEnglish(
    weight: Int,
    height: Int
): String {
    val bmi = weight / (height * height) * 703.07 // 주의: 곱셈 결과가 정수로 변환되어 정확도 저하
    return if (bmi < 18.5) "Underweight"
    else if (bmi < 25) "Normal weight"
    else "Overweight"
}

fun main() {
    val weight = 160 // 파운드 (lb)
    val height = 68 // 인치 (in)
    val status = bmiEnglish(weight, height)
    println(status) // 출력: Underweight
}
```

**핵심 개념:**
- 정수 나눗셈 결과는 정확도를 잃을 수 있으므로, 계산 중간에 `Double` 타입을 사용하는 것이 중요합니다.

## 정수 오버플로우

Kotlin의 `Int` 타입은 제한된 범위 내에서만 작동합니다: `-2^31`부터 `2^31 - 1`까지입니다. 큰 숫자를 더하거나 곱하면 오버플로우가 발생할 수 있어요:

```kotlin
fun main() {
    val i: Int = Int.MAX_VALUE
    println(i + i) // 출력: -2 (오버플로우 결과)
}
```

**핵심 개념:**
- 큰 숫자 연산 시 오버플로우를 주의해야 합니다. 필요한 경우 `Long` 타입을 사용하세요.

---

이렇게 기본적인 숫자 타입과 연산자에 대해 알아보았어요. 이해하기 쉽게 설명드렸으니, 연습해보면서 더 익숙해지세요! 궁금한 점이 있으면 언제든지 물어봐요!