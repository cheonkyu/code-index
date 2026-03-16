# Item 25: 서로 다른 플랫폼 간 재사용을 위해 공통 모듈 추출하기

안녕하세요! 코틀린 프로그래밍 전문가이자 친절한 강사입니다. Effective Kotlin 책의 'Item 25: Reuse between different platforms by extracting common modules'에 대해 자세히 알아보도록 하겠습니다. 이 아이템은 코틀린의 멀티플랫폼 기능을 활용하여 코드 재사용성을 극대화하는 방법을 다루고 있어요.

## 1. 왜 공통 모듈을 추출해야 할까요? (Best Practice)

여러 플랫폼(Android, iOS, Web, Desktop 등)을 지원하는 앱을 개발하다 보면 플랫폼별로 비슷한 로직이 반복되는 경우가 많습니다. 이럴 때마다 코드를 복사-붙여넣기 하다 보면 유지보수가 어려워지고, 버그 발생 가능성이 높아지죠. 

공통 모듈을 추출하면 이러한 문제를 해결할 수 있습니다. 공통 모듈은 플랫폼에 종속되지 않는 로직을 담고 있어, 여러 플랫폼에서 재사용할 수 있습니다. 이렇게 하면:

* **코드 중복 감소:** 코드의 양이 줄어들어 가독성이 높아지고, 유지보수가 쉬워집니다.
* **일관성 유지:** 모든 플랫폼에서 동일한 로직을 사용하므로, 동작 방식이 일관성을 유지합니다.
* **테스트 용이성:** 공통 로직을 한 곳에서 테스트하므로, 테스트가 간편해집니다.

## 2. 공통 모듈 추출 방법

코틀린에서 공통 모듈을 만들려면 `kotlin-multiplatform` 플러그인을 사용해야 합니다. 이 플러그인은 코틀린 컴파일러에게 공통 모듈을 생성하고, 플랫폼별로 적절하게 컴파일하도록 알려줍니다.

**1. 프로젝트 설정:** `build.gradle.kts` 파일에 `kotlin-multiplatform` 플러그인을 추가합니다.

```kotlin
plugins {
    kotlin("multiplatform") version "1.9.22" // 최신 버전 확인!
}
```

**2. 공통 모듈 정의:** `src/commonMain` 디렉터리에 공통 코드를 작성합니다. 이 디렉터리는 모든 플랫폼에서 공유되는 코드를 담습니다.

```kotlin
// src/commonMain/kotlin/com/example/common/MyCommonClass.kt
package com.example.common

fun commonFunction(): String {
    return "This is a common function!"
}
```

**3. 플랫폼별 모듈 정의:**  `src/androidMain`, `src/iosMain`, `src/jsMain` 등 플랫폼별 디렉터리에 해당 플랫폼에 특화된 코드를 작성합니다.

```kotlin
// src/androidMain/kotlin/com/example/common/MyCommonClass.kt
package com.example.common

actual fun commonFunction(): String {
    return "This is a common function on Android!"
}
```

```kotlin
// src/iosMain/kotlin/com/example/common/MyCommonClass.kt
package com.example.common

actual fun commonFunction(): String {
    return "This is a common function on iOS!"
}
```

**4. 기대(Expect) / 실제(Actual) 선언:** `expect` 키워드를 사용하여 공통 모듈에서 인터페이스나 함수를 선언하고, 플랫폼별 모듈에서 `actual` 키워드를 사용하여 해당 인터페이스나 함수를 구현합니다.  위 예제에서 `commonFunction()`이 바로 expect/actual의 예시입니다.

## 3. 고려 사항

* **플랫폼 종속성:** 공통 모듈에는 플랫폼에 종속적인 코드를 넣지 않도록 주의해야 합니다. (예: Android의 `Activity`, iOS의 `UIKit`)
* **테스트:** 공통 모듈을 충분히 테스트하여 모든 플랫폼에서 예상대로 동작하는지 확인해야 합니다.
* **의존성 관리:** 공통 모듈과 플랫폼별 모듈 간의 의존성을 관리해야 합니다.

## 핵심 요약

* 공통 모듈을 추출하여 코드 재사용성을 높이고 유지보수를 간편하게 만들 수 있습니다.
* `kotlin-multiplatform` 플러그인을 사용하여 멀티플랫폼 프로젝트를 설정할 수 있습니다.
* `expect` 키워드로 공통 인터페이스를 정의하고, `actual` 키워드로 플랫폼별 구현을 제공합니다.
* 플랫폼 종속적인 코드는 공통 모듈에 포함하지 않도록 주의해야 합니다.