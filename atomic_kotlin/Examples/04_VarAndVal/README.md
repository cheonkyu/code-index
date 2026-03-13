# var & val: 코틀린 변수와 값의 이해하기

안녕하세요! 코틀린을 처음 접하는 분들을 위해 `var`와 `val`에 대한 간단하고 친근한 설명을 드릴게요. 코틀린에서 변수를 다룰 때 가장 중요한 두 가지 키워드가 바로 `var`와 `val`입니다. 이 두 개념을 이해하면 코드를 더 안전하고 명확하게 작성할 수 있습니다.

## var: 변경 가능한 변수
`var`는 **변경 가능한 변수**를 의미합니다. 이름에서도 알 수 있듯이, 이 변수는 프로그램 실행 중에 값을 여러 번 바꿀 수 있습니다.

### 사용법
- **정의 방법**: `var 변수이름 = 초기값`
- **규칙**: 초기화 이후에도 값을 변경할 수 있습니다.

### 예시
```kotlin
fun main() {
    // [1] whole 변수에 11 저장
    var whole = 11
    // [2] fractional 변수에 1.4 저장
    var fractional = 1.4
    // [3] words 변수에 "Twas Brillig" 저장
    var words = "Twas Brillig"
    
    println(whole)    // 출력: 11
    println(fractional) // 출력: 1.4
    println(words)     // 출력: Twas Brillig
    
    // 값을 변경해보기
    whole = whole + 5  // whole의 값을 16으로 변경
    fractional += 0.1  // fractional의 값을 1.5로 변경
    
    println(whole)    // 출력: 16
    println(fractional) // 출력: 1.5
    println(words)     // 출력: Twas Brillig (변경 없음)
}
```

### 주요 포인트
- `var`로 정의된 변수는 실행 중에 여러 번 값이 바뀔 수 있습니다.
- 예를 들어, `whole` 변수는 처음 11로 설정되었다가 나중에 16으로 변경되었습니다.

## val: 불변 변수
`val`은 **불변 변수**를 의미합니다. 이름에서도 알 수 있듯이, 이 변수는 초기화 후에는 값을 변경할 수 없습니다. 불변 변수는 코드의 안전성과 가독성을 높여줍니다.

### 사용법
- **정의 방법**: `val 변수이름 = 초기값`
- **규칙**: 초기화 이후에는 값을 변경할 수 없습니다.

### 예시
```kotlin
fun main() {
    // whole 변수를 val로 정의 (불변)
    val whole = 11 // [1] 초기화 이후 변경 불가
    // whole = 15  // 오류: Val cannot be reassigned
    
    val fractional = 1.4 // [2] 초기화된 값 유지
    val words = "Twas Brillig" // [3] 초기화된 값 유지
    
    println(whole)    // 출력: 11
    println(fractional) // 출력: 1.4
    println(words)     // 출력: Twas Brillig
}
```

### 주요 포인트
- `val`로 정의된 변수는 초기화 이후에 값을 변경할 수 없습니다.
- 예를 들어, `whole` 변수는 `val`로 정의되었으므로 `whole = 15`와 같은 변경은 오류를 발생시킵니다.
- 불변 변수는 프로그램의 안정성을 높이고, 의도치 않은 변경을 방지합니다.

## 요약
- **`var`**: 값을 여러 번 변경할 수 있는 유연한 변수입니다.
- **`val`**: 초기화 이후 값을 변경할 수 없는 안전하고 명확한 변수입니다.

가능한 경우 `val`을 우선적으로 사용하여 코드의 안정성을 높이세요! 이해가 잘 되셨나요? 더 궁금한 점이 있으면 언제든지 물어보세요!