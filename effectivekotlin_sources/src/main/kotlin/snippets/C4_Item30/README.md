# Item 30: 요소의 가시성 최소화하기

안녕하세요, 초보 코틀린 개발자 여러분! 오늘은 코틀린 프로그래밍에서 중요한 베스트 프랙티스 중 하나인 **요소의 가시성 최소화**에 대해 함께 살펴보겠습니다. 이 주제는 코드의 가독성과 유지보수성을 크게 향상시키는 데 도움이 됩니다.

## 핵심 가이드라인 및 이유 (Best Practice)

### 가이드라인
1. **내부 클래스와 멤버 변수의 가시성 최소화**: 가능한 한 내부 클래스로 선언하고 필요한 경우에만 멤버 변수를 `public`으로 설정하세요. 외부에서 접근이 필요 없는 경우에는 `private` 또는 `internal`로 제한합니다.
2. **불필요한 가시성 지정 제거**: 클래스의 멤버 변수나 함수에 대해 불필요한 가시성 지정을 제거하여 코드를 간결하게 유지하세요.

### 이유
- **유지보수성 향상**: 가시성이 제한되면 코드의 내부 구조를 변경할 때 외부에 미치는 영향을 최소화할 수 있습니다. 예를 들어, 내부 클래스나 멤버 변수의 가시성을 조정하면 외부에서 직접 접근하는 경로가 줄어들어 수정 시 안전성이 높아집니다.
- **가독성 개선**: 불필요한 가시성 지정은 코드를 복잡하게 만들 수 있습니다. 필요한 부분만 가시성을 부여함으로써 코드의 이해를 쉽게 만듭니다.

## 예제 코드

### 내부 클래스 예제
```kotlin
class OuterClass {
    // 외부에서 접근이 필요 없는 내부 클래스
    internal inner class InternalClass {
        private val secretData = "민감한 데이터"
        
        fun revealData() {
            println(secretData) // 내부 클래스 내에서만 접근 가능
        }
    }
}

fun main() {
    val outerInstance = OuterClass()
    // 외부에서 직접 접근 불가 (내부적으로만 사용 가능)
    // outerInstance.InternalClass.secretData // 컴파일 오류 발생
    val internalInstance = outerInstance.InternalClass() // 직접 생성 불가
    internalInstance.revealData() // 가능
}
```

### 멤버 변수 가시성 최소화 예제
```kotlin
class User {
    // 외부에서 직접 접근이 필요 없는 변수
    private val userPreferences = mutableListOf<String>()

    fun updatePreferences(preferences: List<String>) {
        userPreferences.addAll(preferences)
    }

    // 외부에서 직접 사용할 수 있는 인터페이스 제공
    fun getUserInfo(): String {
        return "Preferences: ${userPreferences.joinToString(", ")}"
    }
}

fun main() {
    val user = User()
    user.updatePreferences(listOf("음악", "영화")) // 내부적으로만 직접 접근 가능
    println(user.getUserInfo()) // 외부 인터페이스를 통해 접근 가능
}
```

## 핵심 요약
- 내부 클래스와 멤버 변수의 가시성을 최소화하여 코드의 안정성과 가독성을 향상시킵니다.
- 불필요한 가시성 지정을 제거하여 유지보수와 이해를 용이하게 만듭니다.
- 외부 접근이 필요 없는 부분은 `private` 또는 `internal`로 제한하여 코드 구조를 효과적으로 관리합니다.