# 25. Varargs (가변 인자)

안녕하세요! 오늘은 **Varargs**에 대해 배워볼게요. Varargs는 코틀린에서 여러 개의 인자를 유연하게 받을 수 있게 해주는 기능이에요. 처음에는 조금 헷갈릴 수 있지만, 몇 가지 기본 개념을 이해하면 어렵지 않아요!

## Varargs란 무엇인가요?

Varargs는 **가변 인자**를 의미해요. 함수나 메소드가 여러 개의 인자를 받을 수 있도록 설계되었죠. 사용자가 인자를 몇 개든 넣을 수 있어요. 마치 냄비에 다양한 재료를 넣을 수 있듯이요!

### 기본적인 Varargs 사용 방법

코틀린에서는 `vararg` 키워드를 사용해 가변 인자를 정의할 수 있어요. 함수 정의 시에 뒤에 `**` (별 두 개)를 붙이면 돼요. 예를 들어, 여러 개의 숫자를 받아서 합을 구하는 함수를 만들어볼게요.

```kotlin
fun sum(numbers: Array<Double>) { // 단일 인자 예시 (이 경우는 좀 제한적이죠)
    var total = 0.0
    for (number in numbers) {
        total += number
    }
    println("합: $total")
}

fun sum(numbers: Array<Double>) { // 가변 인자 예시
    var total = 0.0
    for (number in numbers) {
        total += number
    }
    println("합: $total")
}

// 가변 인자 버전 사용 예시
fun main() {
    val numbers1 = arrayOf(1.0, 2.0, 3.0) // 배열로 인자 전달
    sum(numbers1) // 여러 개의 숫자를 받음

    val numbers2 = listOf(4.0, 5.0) // 리스트로도 전달 가능 (리스트는 배열로 변환됨)
    sum(numbers2.toArray()) // 리스트를 배열로 변환하여 전달

    // 인자가 하나만 주어진 경우에도 동작
    sum(10.0) // 단일 숫자 인자도 가능
}
```

### 주요 개념 요약

1. **`vararg` 키워드**: 함수 정의 시 `**`를 붙여 가변 인자를 만듭니다.
   ```kotlin
   fun exampleFunction(values: Array<String>) { ... } // 단일 인자
   fun exampleFunction(values: Array<String>) { ... } // 가변 인자 버전
   ```

2. **인자 전달**:
   - 배열 (`Array`)이나 리스트 (`List`)를 사용해 여러 값 전달 가능.
   - 단일 값만 전달해도 동작합니다. 가변 인자는 유연성을 제공하니까요!

3. **내부 처리**:
   - 코틀린 내부적으로 가변 인자 배열을 처리하므로, 코드는 단일 인자처럼 보이지만 실제로는 여러 값을 받습니다.

### 실제 활용 예시

가변 인자는 다양한 상황에서 유용해요. 예를 들어, 여러 개의 메시지를 받아서 하나의 문자열로 합치는 함수를 만들 수 있어요:

```kotlin
fun concatenateMessages(*messages: String) {
    var result = ""
    for (message in messages) {
        result += message + " "
    }
    println("합쳐진 메시지: $result")
}

fun main() {
    concatenateMessages("안녕", "하세요", "여러분!") // 여러 개의 문자열 인자
    concatenateMessages("반갑습니다") // 단일 문자열 인자
}
```

이렇게 보면, 가변 인자는 함수의 유연성을 크게 높여주는 강력한 도구라는 걸 알 수 있죠! 연습을 통해 점점 익숙해질 거예요. 궁금한 점이 있으면 언제든지 물어봐요! 😊