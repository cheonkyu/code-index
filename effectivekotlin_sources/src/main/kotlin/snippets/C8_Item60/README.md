# Item 60: `let`, `run`, `with`, `apply`, `also`의 차이점을 이해하고 상황에 맞게 사용하세요.

안녕하세요! 코틀린 프로그래밍 전문가이자 여러분의 친절한 강사입니다. 오늘은 Effective Kotlin 책의 중요한 내용 중 하나인 `let`, `run`, `with`, `apply`, `also` 함수의 차이점을 자세히 알아보려고 해요. 이 함수들은 코틀린에서 객체의 멤버에 접근하거나 객체를 조작하는 데 매우 유용하지만, 처음 접하는 분들은 각각의 역할과 차이점이 헷갈릴 수 있어요. 걱정 마세요! 차근차근 쉽게 설명해 드릴게요.

## 왜 이 함수들을 알아야 할까요?

코틀린은 간결하고 가독성 좋은 코드를 작성하는 데 중점을 둡니다. `let`, `run`, `with`, `apply`, `also` 함수들은 이러한 코틀린의 철학을 반영하며, 다음과 같은 장점을 제공합니다.

*   **가독성 향상:** 복잡한 연산이나 객체 조작을 더 읽기 쉽고 의미 있는 방식으로 표현할 수 있습니다.
*   **null 안전성:** `let`과 `also`는 null 안전하게 객체에 접근할 수 있도록 도와줍니다.
*   **코드 간결화:** 불필요한 코드를 줄이고 코드를 더 간결하게 만들어줍니다.

## 각 함수들의 역할과 차이점

각 함수는 객체를 인자로 받아, 그 객체에 대해 특정 작업을 수행합니다. 중요한 것은 각 함수가 객체를 인자로 받는 방식과 반환하는 값이 다르다는 점이에요.

### 1. `let` 함수

*   **역할:** 객체를 `it`이라는 이름으로 인자로 받아서, `it`에 대해 특정 작업을 수행하고, 그 결과값을 반환합니다.
*   **특징:** null 안전하게 사용할 수 있습니다. 객체가 null이 아니면 작업이 수행되고, null이면 함수 자체가 호출되지 않습니다.
*   **사용 예시:**
    ```kotlin
    val name: String? = "Kotlin"
    val length = name?.let {
        println("Name is not null") // name이 null이 아닐 때만 실행
        it.length
    } ?: 0 // name이 null이면 length는 0이 됩니다.

    println("Length of name: $length")
    ```
    이 예제에서 `name`이 null이 아니면 `let` 블록이 실행되어 문자열의 길이를 계산하고, null이면 `?:` 연산자를 통해 `length`는 0으로 설정됩니다.

### 2. `run` 함수

*   **역할:** `let`과 유사하지만, `it`이라는 이름 대신 객체를 직접 접근할 수 있습니다. 또한, 객체 자체를 반환합니다.
*   **특징:** 객체가 null이 아닌 경우에만 호출됩니다.
*   **사용 예시:**
    ```kotlin
    val message = "Hello, Kotlin!"
    val result = message.run {
        println("Message: $this") // this를 사용하여 객체에 직접 접근
        length
    }

    println("Result: $result")
    ```
    여기서 `run` 블록 내에서 `this` 키워드를 사용하여 `message` 객체에 직접 접근할 수 있습니다.

### 3. `with` 함수

*   **역할:** 객체를 인자로 받아, 해당 객체의 멤버에 직접 접근할 수 있도록 해줍니다. 마지막 표현식의 결과값을 반환합니다.
*   **특징:** 객체가 null인 경우 `NullPointerException`이 발생할 수 있습니다.
*   **사용 예시:**
    ```kotlin
    data class Person(val name: String, val age: Int)

    val person = Person("Alice", 30)
    with(person) {
        println("Name: $name, Age: $age")
        // person 객체의 멤버에 직접 접근
    }
    ```
    `with` 블록 내에서 `person` 객체의 멤버(`name`, `age`)에 직접 접근할 수 있습니다.

### 4. `apply` 함수

*   **역할:** 객체를 인자로 받아, 해당 객체에 대해 설정을 수행하고, 객체 자체를 반환합니다.
*   **특징:** 객체를 설정하는 데 유용하며, 주로 객체 생성을 위한 빌더 패턴과 함께 사용됩니다.
*   **사용 예시:**
    ```kotlin
    data class Config(var host: String = "", var port: Int = 0)

    val config = Config().apply {
        host = "localhost"
        port = 8080
    }

    println("Host: ${config.host}, Port: ${config.port}")
    ```
    `apply` 함수를 사용하면 객체를 생성하고 즉시 속성을 설정할 수 있습니다.

### 5. `also` 함수

*   **역할:** 객체를 인자로 받아, 객체에 대해 부가적인 작업을 수행하고, 객체 자체를 반환합니다.
*   **특징:** 객체 자체를 변경하지 않고, 단순히 추가적인 작업을 수행할 때 유용합니다. `let`과 마찬가지로 null 안전하게 사용할 수 있습니다.
*   **사용 예시:**
    ```kotlin
    val numbers = mutableListOf<Int>(1, 2, 3)
    numbers.also {
        println("Original list: $it")
    }.add(4)

    println("Modified list: $numbers")
    ```
    `also` 블록 내에서 `numbers` 리스트를 출력하고, 그 후 리스트에 4를 추가합니다.

## 어떤 함수를 사용해야 할까요?

| 함수     | 반환값     | 객체 접근 방식 | Null 안전성 | 주요 사용처                                 |
| -------- | ---------- | -------------- | ----------- | ------------------------------------------- |
| `let`    | 결과값     | `it`           | O           | Null 처리, 값 변환                            |
| `run`    | 객체 자체  | `this`         | X           | 객체 설정 및 결과 반환                       |
| `with`   | 결과값     | 직접 접근      | X           | 객체 설정 및 작업 수행                       |
| `apply`  | 객체 자체  | 직접 접근      | X           | 객체 설정 및 빌더 패턴                       |
| `also`   | 객체 자체  | `it`           | O           | 부가적인 작업 수행, 로깅, 디버깅              |

## 핵심 요약

*   `let`, `run`, `with`, `apply`, `also`는 코틀린에서 객체를 조작하고 가독성을 높이는 데 사용되는 함수입니다.
*   각 함수는 객체를 받는 방식, 반환값, null 안전성 측면에서 차이가 있습니다.
*   상황에 맞는 함수를 선택하여 코드를 간결하고 명확하게 작성하는 것이 중요합니다.
*   특히, `let`과 `also`는 null 안전하게 객체에 접근할 수 있다는 점을 기억하세요!

오늘 배운 내용을 바탕으로 코틀린 코드를 더욱 효율적으로 작성하시길 바랍니다. 질문이 있으시면 언제든지 편하게 물어보세요!