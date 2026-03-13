# 72. CompanionObjects: 함께 배우는 코틀린 친구들

안녕하세요, 코틀린 초보자 여러분! 이번 챕터에서는 코틀린에서 클래스와 함께 사용하는 특별한 친구인 **컴파니 객체(Companion Objects)**에 대해 배워볼게요. 이해하기 쉽게 설명해드릴게요!

## 컴파니 객체란?

컴파니 객체는 클래스와 밀접하게 연결된 특별한 객체입니다. 일반적인 멤버 함수들은 특정 클래스 인스턴스에 대해 작동하지만, 컴파니 객체 내부의 함수와 필드는 클래스 자체에 대한 것이에요. 쉽게 말해, 컴파니 객체는 클래스와 함께 사용되는 공용 리소스나 공통 기능을 담고 있는 친구라고 생각하면 돼요.

### 기본 구조와 사용 예

#### 클래스 정의 예시

아래 코드를 보세요. `WithCompanion` 클래스와 그 안에 있는 컴파니 객체를 보면 이해가 쉬울 거예요:

```kotlin
package companionobjects

import atomictest.eq // 테스트를 위한 라이브러리

class WithCompanion {
    // 컴파니 객체 정의
    companion object {
        val i = 3      // 클래스 공통으로 사용할 변수
        fun f() = i * 3 // 컴파니 객체 내부 함수
    }

    // 컴파니 객체 요소에 접근 가능
    fun g() = i + f()  // 클래스 멤버는 컴파니 객체 요소에 직접 접근 가능

    // 컴파니 객체 내부 함수 직접 호출도 가능
    fun WithCompanion.Companion.h() = f() * i  // 컴파니 객체 내부 함수 호출
}

fun main() {
    val wc = WithCompanion()  // 클래스 인스턴스 생성
    wc.g() eq 12            // wc.g() 호출 결과 확인
    WithCompanion.i eq 3   // 클래스 이름으로 컴파니 객체 요소 접근
    WithCompanion.f() eq 9 // 컴파니 객체 함수 호출 결과 확인
    WithCompanion.h() eq 27 // 컴파니 객체 내부 함수 호출 결과 확인
}
```

#### 컴파니 객체 접근 방법
- **클래스 이름으로 접근**: `WithCompanion.i` 또는 `WithCompanion.f()`로 사용
- **클래스 멤버 내 접근**: 클래스 멤버에서 컴파니 객체 요소에 직접 접근 가능 (예: `g()`)

### 컴파니 객체 명명하기
컴파니 객체는 기본적으로 `Companion`이라는 이름을 가질 수 있지만, 원하는 이름을 지정할 수도 있어요:

```kotlin
package companionobjects

import atomictest.eq

class WithNamed {
    companion object Named {
        fun s() = "from Named"  // 컴파니 객체에 이름 부여
    }
}

class WithDefault {
    companion object {
        fun s() = "from Default"  // 기본 이름 사용
    }
}

fun main() {
    WithNamed.s() eq "from Named"  // Named 컴파니 객체 호출
    WithNamed.Named.s() eq "from Named" // 컴파니 객체 이름으로 호출
    WithDefault.s() eq "from Default"  // 기본 이름 사용
    WithDefault.Companion.s() eq "from Default" // 기본 이름으로 호출 가능
}
```

### 컴파니 객체의 특징
1. **공통 저장소**: 컴파니 객체 내의 필드는 모든 클래스 인스턴스가 공유합니다. 예를 들어:

   ```kotlin
   package companionobjects

   import atomictest.eq

   class WithObjectProperty {
       companion object {
           private var n: Int = 0  // 모든 인스턴스가 공유하는 변수
       }

       fun increment() = ++n  // 증가 함수 호출
   }

   fun main() {
       val a = WithObjectProperty()
       val b = WithObjectProperty()
       a.increment() eq 1  // 첫 번째 호출 결과
       b.increment() eq 2  // 두 번째 호출 결과
       a.increment() eq 3  // 세 번째 호출 결과
   }
   ```

2. **확장 함수**: 컴파니 객체 내부의 함수는 클래스 외부에서도 확장 함수로 사용 가능합니다.

### 컴파니 객체 활용 팁
- **공통 기능 분리**: 클래스와 관련된 공통 기능을 컴파니 객체에 모아 관리하면 코드가 더 깔끔해집니다.
- **인스턴스 생성 없이 함수 호출**: 컴파니 객체 내부 함수는 클래스 인스턴스 없이도 호출 가능합니다.

### 요약
- **컴파니 객체**는 클래스와 함께 공유되는 공용 리소스나 기능을 담고 있는 특별한 객체입니다.
- **접근 방법**: 클래스 이름으로 직접 접근하거나 클래스 내부에서 쉽게 접근 가능합니다.
- **공유 저장소**: 컴파니 객체 내부 필드는 모든 인스턴스가 공유합니다.

이제 컴파니 객체에 대해 조금 더 친숙해졌기를 바라요! 다음 챕터에서도 재미있는 코틀린 이야기 계속 이어가볼게요. 질문이 있으면 언제든지 물어봐요!