# 20. Visibility

안녕하세요! 오늘은 Kotlin에서 변수와 함수의 **Visibility**에 대해 배워볼게요. Visibility는 코드 내에서 클래스나 함수 외부에서 해당 멤버(변수나 함수)에 접근할 수 있는지를 결정하는 중요한 개념이에요. 초보자분들도 쉽게 이해할 수 있도록 단계별로 설명해드릴게요.

## 기본 개념

Visibility는 다음과 같은 키워드를 사용해 제어할 수 있어요:

- **public**: 가장 넓은 범위에서 접근 가능합니다. 모든 클래스와 패키지 내외부에서 접근 가능해요.
- **internal**: 동일한 패키지 내에서만 접근 가능합니다. 외부 패키지에서는 접근할 수 없어요.
- **protected**: 상속 관계에서 같은 패키지 내에서만 접근 가능합니다. 상속받은 클래스에서만 접근 가능해요.
- **private**: 현재 클래스 내에서만 접근 가능합니다. 외부에서는 절대 접근할 수 없어요.

### 요약
- **public**: 가장 넓은 범위 (모든 클래스와 패키지)
- **internal**: 동일 패키지 내에서만
- **protected**: 상속 관계 내 동일 패키지에서만
- **private**: 현재 클래스 내에서만

## 예제 코드로 이해하기

아래 예제를 통해 각 Visibility 키워드가 어떻게 작동하는지 확인해볼게요.

### public 예제
```kotlin
// public 키워드를 사용한 클래스
class MyClassPublic {
    public val publicVariable: String = "I'm public!"

    public fun publicFunction() {
        println("This is a public function!")
    }
}

fun main() {
    val obj = MyClassPublic()
    println(obj.publicVariable)  // 접근 가능: 출력 결과: "I'm public!"
    obj.publicFunction()        // 호출 가능: 출력 결과: "This is a public function!"
}
```

**해설**: `publicVariable`과 `publicFunction`은 클래스 외부에서도 자유롭게 접근 및 호출이 가능해요.

### internal 예제
```kotlin
// internal 키워드를 사용한 클래스
class MyClassInternal {
    internal val internalVariable: String = "I'm internal!"

    internal fun internalFunction() {
        println("This is an internal function!")
    }
}

fun main() {
    val obj = MyClassInternal()  // 외부에서 객체 생성 불가
    // println(obj.internalVariable)  // 컴파일 에러: 접근 불가
    // obj.internalFunction()       // 컴파일 에러: 호출 불가
}
```

**해설**: `internalVariable`과 `internalFunction`은 동일한 패키지 내에서만 접근 및 호출이 가능해요. 외부 패키지에서는 접근할 수 없어요.

### protected 예제 (상속 관계 필요)
```kotlin
// protected 키워드를 사용한 클래스
open class ParentClass {
    protected val protectedVariable: String = "I'm protected!"

    protected fun protectedFunction() {
        println("This is a protected function!")
    }
}

class ChildClass : ParentClass() {
    fun useProtected() {
        println(ChildClass().protectedVariable)  // 접근 가능: 컴파일 에러 없음 (동일 패키지 내)
        ChildClass().protectedFunction()       // 호출 불가: 컴파일 에러 (동일 패키지 내에서만 가능)
    }
}

fun main() {
    val child = ChildClass()
    child.useProtected()  // 출력 결과: "I'm protected!" (보호된 멤버 접근)
}
```

**해설**: `protectedVariable`과 `protectedFunction`은 상속 관계 내 동일 패키지에서만 접근 및 호출이 가능해요. 위 예제에서는 `ChildClass`에서 접근 가능합니다.

### private 예제
```kotlin
// private 키워드를 사용한 클래스
class MyClassPrivate {
    private val privateVariable: String = "I'm private!"

    private fun privateFunction() {
        println("This is a private function!")
    }
}

fun main() {
    val obj = MyClassPrivate()
    // println(obj.privateVariable)  // 컴파일 에러: 접근 불가
    // obj.privateFunction()        // 컴파일 에러: 호출 불가
}
```

**해설**: `privateVariable`과 `privateFunction`은 현재 클래스 내에서만 접근 및 호출이 가능해요. 외부에서는 절대 접근할 수 없어요.

## 마무리

이렇게 Visibility 키워드를 사용하면 코드의 접근성을 세밀하게 제어할 수 있어요. 각 키워드의 범위를 잘 이해하고 적절히 사용하면 더 안전하고 효율적인 코드를 작성할 수 있답니다. 연습을 통해 점점 더 자연스럽게 적용할 수 있을 거예요! 궁금한 점이 있으면 언제든지 물어보세요.