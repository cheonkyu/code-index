# 79. Extension Lambdas

안녕하세요, 초보자 여러분! 오늘은 코틀린 프로그래밍에서 조금 특별한 개념인 **Extension Lambdas**에 대해 배워볼게요. 쉽게 말해서, Extension Lambdas는 마치 확장 함수 같은 역할을 하지만, 그 정의 방식이 조금 다르답니다. 이해하기 쉽게 단계별로 설명해드릴게요.

## 기본 개념

### 정의와 사용법
Extension Lambda는 함수 리터럴(함수 표현식) 중에서 특정 객체를 수신자(receiver)로 가지는 람다 표현식입니다. 주로 확장 함수와 유사하게 사용되지만, 람다 형태로 작성되죠.

#### 예제 코드: `Vanbo.kt`

```kotlin
package extensionlambdas
import atomictest.eq

// 보통의 람다 정의
val va: (String, Int) -> String = { str, n ->
    str.repeat(n) + str.repeat(n)  // "VanboVanboVanboVanbo"
}

// 확장 람다 정의 (Extension Lambda)
val vb: String.(Int) -> String = {
    this.repeat(it) + repeat(it)  // "VanboVanboVanboVanbo"
}

fun main() {
    // 보통 람다 사용 예시
    va("Vanbo", 2) eq "VanboVanboVanboVanbo"
    
    // 확장 람다 사용 예시
    "Vanbo".vb(2) eq "VanboVanboVanboVanbo"  // 문자열 직접 호출 가능
    vb("Vanbo", 2) eq "VanboVanboVanboVanbo"  // 함수 호출 형태 가능
    
    // 주의: 아래 코드는 컴파일 에러가 발생해요!
    // "Vanbo".va(2) // 에러: 확장 람다 형태로 호출 불가능
}
```

**핵심 포인트:**
- `va`는 일반적인 람다로, `(String, Int) -> String` 타입을 가지고 있어요.
- `vb`는 확장 람다로, `String.(Int) -> String` 형태로 정의되었어요. 여기서 `this`는 람다가 적용되는 `String` 객체를 의미해요.
- 확장 람다는 객체를 직접 호출할 수 있게 해주며, `this` 키워드를 사용해 해당 객체의 멤버를 직접 접근할 수 있어요.

## 여러 매개변수를 가진 Extension Lambdas

확장 람다도 여러 매개변수를 가질 수 있어요. 예를 들어보죠:

#### 예제 코드: `Parameters.kt`

```kotlin
package extensionlambdas
import atomictest.eq

// 단일 매개변수 확장 람다
val zero: Int.() -> Boolean = { this == 0 }  // 정수가 0인지 체크

// 두 개의 매개변수 확장 람다
val one: Int.(Int) -> Boolean = { this % it == 0 }  // 첫 번째 숫자가 두 번째 숫자로 나누어 떨어지는지 체크

// 세 개의 매개변수 확장 람다
val two: Int.(Int, Int) -> Boolean = { arg1, arg2 -> this % (arg1 + arg2) == 0 }  // 특정 조건 체크

// 네 개의 매개변수 확장 람다
val three: Int.(Int, Int, Int) -> Boolean = { arg1, arg2, arg3 -> this % (arg1 + arg2 + arg3) == 0 }  // 더 복잡한 조건 체크

fun main() {
    0.zero() eq true  // 0은 항상 true
    10.one(10) eq true  // 10은 10으로 나누어 떨어짐
    20.two(10, 10) eq true  // 복잡한 조건 체크
    30.three(10, 10, 10) eq true  // 네 개의 매개변수로 체크
}
```

**핵심 포인트:**
- 매개변수가 늘어날수록 람다 내에서 접근할 때 `arg1`, `arg2` 등으로 명명할 수 있어요. 만약 명확하지 않다면 매개변수 이름을 명시하는 것이 좋아요.

## 함수 매개변수로 사용하기

확장 람다는 함수 매개변수로도 자주 사용됩니다:

#### 예제 코드: `FunctionParameters.kt`

```kotlin
package extensionlambdas
class A {
    fun af() = 1
}

class B {
    fun bf() = 2
}

// 일반 람다 형태
fun f1(lambda: (A, B) -> Int) = lambda(A(), B())

// 확장 람다 형태
fun f2(lambda: A.(B) -> Int) = A().lambda(B())

fun lambdas() {
    f1 { aa, bb -> aa.af() + bb.bf() }  // 일반 람다 사용
    f2 { af() + it.bf() }  // 확장 람다 사용 (더 간결)
}
```

**핵심 포인트:**
- 확장 람다는 함수 호출 시 더 간결한 문법을 제공합니다. 특히 수신 객체가 명확한 경우에 유용해요.

## 반환 타입이 Unit인 경우

확장 람다가 `Unit`을 반환할 때는 반환 값에 주의할 필요가 없어요:

#### 예제 코드: `LambdaUnitReturn.kt`

```kotlin
package extensionlambdas
fun unitReturn(lambda: A.() -> Unit) = A().lambda()  // Unit 반환 시 무시
fun nonUnitReturn(lambda: A.() -> String) = A().lambda()  // 특정 타입 반환 시 주의 필요

fun lambdaUnitReturn () {
    unitReturn {
        "Unit은 반환 값을 무시해요"  // 어떤 문자열이든 가능해요
        "그 외 어떤 타입이든 가능해요..."
        ""  // 빈 문자열도 가능해요
    }
    
    nonUnitReturn {
        "특정 타입을 반환해야 해요"  // 잘못된 타입 반환은 오류 발생
    }
    // nonUnitReturn { }  // 컴파일 에러 발생 (타입 불일치)
}
```

**핵심 포인트:**
- `Unit` 반환 시에는 실제 결과 값을 무시하므로 자유롭게 사용 가능해요. 하지만 특정 타입을 반환해야 하는 경우에는 타입을 정확히 지켜야 해요.

## 요약
- **Extension Lambdas**는 확장 함수와 유사하지만 람다 형태로 작성되어 더 유연하게 사용할 수 있어요.
- `this` 키워드를 사용해 객체 멤버에 직접 접근 가능해요.
- 여러 매개변수를 가질 수 있으며, 함수 매개변수로도 많이 활용되요.
- `Unit` 반환 시에는 결과 값을 무시해도 괜찮아요.

이제 코틀린의 확장 람다에 대해 좀 더 친숙해졌길 바라요! 연습을 통해 더 많은 것을 배우실 수 있을 거예요. 질문이 있으면 언제든지 물어보세요!