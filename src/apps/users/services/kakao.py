import httpx

from ...oauth.models.responses import KakaoUserMeResponse


async def get_user_profile(access_token: str) -> KakaoUserMeResponse:
    """
        GET/POST /v2/user/me HTTP/1.1
        Host: kapi.kakao.com
        Authorization: Bearer {ACCESS_TOKEN}
        Content-type: application/x-www-form-urlencoded;charset=utf-8
    """
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://kapi.kakao.com/v2/user/me",
            headers={
                "authorization": f"Bearer {access_token}",
                "content-type": (
                    "application/x-www-form-urlencoded;charset=utf-8"
                ),
            },
        )
        return KakaoUserMeResponse(**response.json())
