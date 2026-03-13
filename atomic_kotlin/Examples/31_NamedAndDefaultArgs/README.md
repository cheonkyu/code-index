# 31. NamedAndDefaultArgs

안녕하세요! 오늘은 코틀린 프로그래밍에서 **Named Arguments**와 **Default Arguments**에 대해 배워볼게요. 이 두 가지 개념은 함수 호출을 더 직관적이고 유연하게 만들어주는 중요한 기능입니다. 초보자분들도 쉽게 이해할 수 있도록 친근하게 설명해드릴게요.

## Named Arguments란?

**Named Arguments**는 함수의 인자를 이름을 사용해서 지정하는 방식입니다. 이렇게 하면 함수 호출 시 인자의 순서를 걱정할 필요가 없어지고, 코드의 가독성을 크게 향상시킬 수 있어요.

### 예제 코드

```kotlin
fun configurePerson(name: String = "Unknown", age: Int = 0, occupation: String = "Unemployed") {
    println("이름: $name, 나이: $age, 직업: $occupation")
}

// Named Arguments 사용 예시
configurePerson(name = "철수", age = 25)  // 이름과 나이만 지정
configurePerson(occupation = "학생", age = 18)  // 직업과 나이만 지정
configurePerson(name = "영희", age = 30, occupation = "교사")  // 모든 인자 지정
```

### 설명
- 위 코드에서 `configurePerson` 함수는 세 가지 파라미터를 가지고 있습니다: `name`, `age`, `occupation`.
- 함수 호출 시 인자를 이름으로 지정하면, 인자의 순서에 상관없이 원하는 값을 쉽게 전달할 수 있어요.
- 예를 들어, `name`과 `age`만 지정하면 `occupation`은 기본값 `"Unemployed"`로 설정됩니다.

## Default Arguments란?

**Default Arguments**는 함수 정의 시 특정 인자에 기본값을 미리 설정하는 것을 의미합니다. 이렇게 하면 해당 인자를 호출 시 명시하지 않아도 기본값이 자동으로 적용되므로 코드가 더 간결해집니다.

### 예제 코드

```kotlin
fun greet(name: String = "손님님", greeting: String = "안녕하세요") {
    println("$greeting, $name!")
}

// Default Arguments 사용 예시
greet()  // 기본값 사용
greet("영희", "안녕")  // 일부 인자만 지정
greet(name = "철수", greeting = "반갑습니다")  // 모든 인자 지정
```

### 설명
- `greet` 함수는 `name`과 `greeting` 두 개의 인자를 가지고 있습니다.
- `name`은 기본값 `"손님님"`, `greeting`은 `"안녕하세요"`로 설정되어 있어요.
- 함수 호출 시 인자를 명시하지 않으면 기본값이 자동으로 적용됩니다.
- 예를 들어, `greet()`를 호출하면 `"안녕하세요, 손님님!"`이 출력됩니다.

## 핵심 요약

- **Named Arguments**: 함수 인자를 이름으로 지정하여 가독성을 높이고 순서에 상관없이 호출 가능.
- **Default Arguments**: 함수 정의 시 기본값을 설정하여 필요 없는 인자를 생략할 수 있게 함으로써 코드를 간결하게 만듦.

이렇게 Named Arguments와 Default Arguments를 활용하면 코틀린 코드를 더 직관적이고 유지보수하기 쉬운 방향으로 작성할 수 있어요. 궁금한 점이 있으면 언제든지 물어봐 주세요! 🚀