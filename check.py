import requests
import time
import random
import os
import uuid
import json
import webbrowser
webbrowser.open('https://t.me/tols_python')
from user_agent import *
ID = input('ENTER YOUR ID => ')

token = input('ENTER UOUR TOKEN => ')

os.system('clear')

def ss():
	while True:
		
		yy = '5678'
		
		y = int(''.join(random.choice(yy)for r in range(1)))
		
		num = 'qwertyuiopasdfghjklzxcvbnm1234567890_.'
		email = str(''.join(random.choice(num)for r in range(y)))
		cookies = {
		    'ig_did': 'C5000B14-C007-4297-931D-988B622F5426',
		    'datr': 'L0h4aHX-XpN43taBi2bCfZ-B',
		    'ig_nrcb': '1',
		    'mid': 'aHhILwABAAFJkpRVlAEioZBcPfhc',
		    'ps_l': '1',
		    'ps_n': '1',
		    'dpr': '3.0234789848327637',
		    'csrftoken': 'FpVUS77tTdF3iU99uAHLtmFMpm6YI6Xo',
		    'wd': '891x715',
		}
		
		headers = {
		    'authority': 'www.instagram.com',
		    'accept': '*/*',
		    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
		    'content-type': 'application/x-www-form-urlencoded',
		    # 'cookie': 'ig_did=C5000B14-C007-4297-931D-988B622F5426; datr=L0h4aHX-XpN43taBi2bCfZ-B; ig_nrcb=1; mid=aHhILwABAAFJkpRVlAEioZBcPfhc; ps_l=1; ps_n=1; dpr=3.0234789848327637; csrftoken=FpVUS77tTdF3iU99uAHLtmFMpm6YI6Xo; wd=891x715',
		    'origin': 'https://www.instagram.com',
		    'referer': 'https://www.instagram.com/',
		    'sec-ch-prefers-color-scheme': 'dark',
		    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
		    'sec-ch-ua-full-version-list': '"Chromium";v="137.0.7337.0", "Not/A)Brand";v="24.0.0.0"',
		    'sec-ch-ua-mobile': '?0',
		    'sec-ch-ua-model': '""',
		    'sec-ch-ua-platform': '"Linux"',
		    'sec-ch-ua-platform-version': '""',
		    'sec-fetch-dest': 'empty',
		    'sec-fetch-mode': 'cors',
		    'sec-fetch-site': 'same-origin',
		    'user-agent': str(generate_user_agent()),
		    'x-asbd-id': '359341',
		    'x-csrftoken': 'FpVUS77tTdF3iU99uAHLtmFMpm6YI6Xo',
		    'x-ig-app-id': '936619743392459',
		    'x-ig-www-claim': '0',
		    'x-instagram-ajax': '1026443473',
		    'x-requested-with': 'XMLHttpRequest',
		    'x-web-session-id': 'hh9c0s:nd6o5c:bgm3kz',
		}
		t = str(time.time()).split(".")[0]
		data = {
		    'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{t}:jdndndifjd',
		    'caaF2DebugGroup': '0',
		    'isPrivacyPortalReq': 'false',
		    'loginAttemptSubmissionCount': '0',
		    'optIntoOneTap': 'false',
		    'queryParams': '{}',
		    'trustedDeviceRecords': '{}',
		    'username': email,
		    'jazoest': '22663',
		}
		
		response = requests.post('https://www.instagram.com/api/v1/web/accounts/login/ajax/', cookies=cookies, headers=headers, data=data).text
		
		if '"user":true' in response:
			print(f'GOOD INS : {email}')
		
			cookies = {
			    'A1': 'd=AQABBByTsGgCEKYz4tiek5VXeuYqYhRSuH8FEgEBAQHksWi6aFx5yyMA_eMCAA&S=AQAAAh_aWV597HX_B6CpRV6W_JQ',
			    'A3': 'd=AQABBByTsGgCEKYz4tiek5VXeuYqYhRSuH8FEgEBAQHksWi6aFx5yyMA_eMCAA&S=AQAAAh_aWV597HX_B6CpRV6W_JQ',
			    'A1S': 'd=AQABBByTsGgCEKYz4tiek5VXeuYqYhRSuH8FEgEBAQHksWi6aFx5yyMA_eMCAA&S=AQAAAh_aWV597HX_B6CpRV6W_JQ',
			    'cmp': 't=1756402490&j=0&u=1---',
			    'gpp': 'DBAA',
			    'gpp_sid': '-1',
			    '_awl': '2.1756402496.5-35f630b61b5391b578689036f67a5ec0-6763652d6575726f70652d7765737431-0',
			    '_ga': 'GA1.1.141835662.1756402527',
			    'AS': 'v=1&s=SG5ze1gk&d=A68b1e612|VWil.oX.2Tp3vjheAtEMVZIR7Ix9PhNbAkETCuz1PaS0At7tBcq9e_EDBF3VQ8Ra5.4I8tC6Tq6UcHmGnw_swvReLSLLGqVLGw6cBoX8rd73qzirWyLJeiSXXLPROo7737SabcnLLIxG8uZPRp8S7zg0wIMet6D4Lt7ZgLGTf4JsZgT_6vFOChFGwMuQl.zbmovQX7FmJF.4NnPApyNlwQTisb9lHBywdDGjAFGM04z5x3Yzxr57ldQ_DRSlwa.qO.wqsgaCEB3TPO0dckvCiNbE96Nj2EpbURCcBIcIrdzqe2KcOnuPwxBdw7VKsTV.B4d4w25x3P8Yo94s.nS.tiwKLwIrGrJOyuKR9C6mr7xCG_MmPNcqup6x2nfqlSLaSZ4bMuQpGkPLo_5dfRFQ7UlZLRAPgG6Q0EMdVHl1X5gPtxo.YA5mIt5MEjSbOjxk8XrfNqhcQQkFc2coj.IOkevNLnoCB2b9UPYMmGc6gjNZlqCFCD.bG4JapmvLJT15rE4ADMYmYEXBK4cIZgsXk0XShS6soUAtcRlGTp2.DNrXiSCzjBzAP.Y1w_KxZU_YheW9B_i6OXKSNcCkk0.TK8_lFxSYzxMoyEJ_IkBZunjhR_EUx3ck_6ANfYghJxxHctgwoAAt0LZBYjDD8cDmAid2Iddu.YZNQ5zgew3otHGhlrlYPjo5PqJIMat44Tsr8aFzm3P4jqavggem3oTQDipw7kQJe6O2Zfv.DxJwFU62tox6g82kDb2HM_6e7oZ5S7YckeT1IOSbsbU9TsmiE_b4l__aJ5f0o5yj6IY91lRWdhOzXVGKRsN3p_u6X9Fbb6VPtjvol8xdZNKV5J09o2vjweyilsqEqXrdDJLNiJAXXqsU.bxqJDtmxhojEAxCv9_AZ_miW9REzOqijCUxm2jc5DwkOWUho5SEZGpjlTNjHMh4Xv3O42peFP09uMas0Z6CAEZKMYIZhPev1y8qm6EkAUKgkQ42GLtiGai_xmpSgRxAcOivWGF5yUOISK12HDa.8dFAY677wrIwd_ApISgwSgxRyfYE_5zGCUud_lHCvrU6_8FrNl3GxCwoTgConWipY73UFCp.6FAQv9OUTCWLwqsE3n8s_N.FkJRhrFn8Ch1gkdePY1mhTQYkDQA15qNlr1Ap5yLmyL6LZ3ZASOR8I.lGZQWmnJ4brt4LsFxtD1o.Uiw161msZwR.4X1oO.Gjh5TVDlVpx6ig8bUYTBMg3b4Hvw--~A|B68b1e59f|F0aZT83.2TraoyWsNVK3vj3REYQmzD.5IqGKyVtCHkkIZ0yxunOVb_yWvC_PRHDSypDIfBY5IK4gtAF3HN8JKRHogG5.CLkDMG922zGtud.t0ofk0j.H33abLKkA_cvHc9OteDjgL4Hpz_hU2epmCZoeGjwWzPUgDk5_p0vBExqay1Y_NjMDgIUxkFi.Xpm9BjSS7M98Z12eZn1QMZF_v71c4AzyI4V2kKpPlDmKOnuGrWdw.hdzULLMXffKX_3ng79hTKHbhjHE0EhT57FnCLztZ2LeqhGge6ZWoef0iyxGmFkOli46ZRtyunfNI9hHgWM4IFVc.tkCoFFpQablh_3iXYzuc5944Jrnv2tj03mtldAnOtQtQdyzMtt_DDkjbzBkBnETirFLuLHbgwEVjzUj7UiLikCXebjQiuRhFe5ID27azWyPF2xVVYiPm9VKLxI6y7BphW8blqrTCnFmfzCEGTxboJorfgpZtX.hdxx8yg6JXfHddDdwCMQJbLsarrydLRJY75.oXrhyBaehem4f5LhNIWRUzi2KeyPWTiHuadBF2vV5TEuiGevOkqC4z8tFXqqm_YN_kVBJkjSXaIpoNPNjQ3CrKmc3kpWAqqHYKdHDs1j2_KC6xgaF_nUc615CNSHsKMX_ZL4qITMnHyJno3HfjGzbgTLtJbyN4WC.lY_2Q0ffdQHgH1mb1GGuTXsJWVmREa7fTC..BAZ9gRXPjIyCAmgz0U8P6Kv78bigfMdURSBIJO49UBTCnv5.O2H03O9ryCeD1IymZ1jJeASg_OXfD4WTCbNKnAklQdnnk.MPUjKXm1doQyH0APOfcXCBSNHJr6y3w3CZgT2AKuW5CcFIzuZe6ZUwtGlu5eOCAQylhES0kPHJIu8BF1TKFYMNKArfl_g6Fa4s.MpmUr9asFh3mxw585sfcZjLv0Q06TIVs8JIPUlTrPpN_ZFoA3BjATTqPR0dRerhbXjkPl_4OSqzKqPMv5yYYuAjac7jITZWu3SsGsscezqeWCVreC.QLrGR5XApCn.BeX1uN83bvF3ye__P30jRZvwIKNbDlq45IrysN1wHjBUVeL_UBpyLVQ1s.AJnGboDXYPkrKI8hVrR3ZlIl78mkDDVlt9EWXG2Ryvf00MtnkWrrXRnmdjbDFjcgOo1MDdX570iIHnrlqfEp1WhSdN0FzcFjRIEHUWjRHFZqChwFFJulcvv62e6yPOzJyIsb3UW635yccEWaEWBOIU-~A',
			    '_ga_7XMXL3P19Q': 'GS2.1.s1756402525$o1$g1$t1756402849$j60$l0$h0',
			}
			
			headers = {
			    'authority': 'login.aol.com',
			    'accept': '*/*',
			    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
			    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
			    # 'cookie': 'A1=d=AQABBByTsGgCEKYz4tiek5VXeuYqYhRSuH8FEgEBAQHksWi6aFx5yyMA_eMCAA&S=AQAAAh_aWV597HX_B6CpRV6W_JQ; A3=d=AQABBByTsGgCEKYz4tiek5VXeuYqYhRSuH8FEgEBAQHksWi6aFx5yyMA_eMCAA&S=AQAAAh_aWV597HX_B6CpRV6W_JQ; A1S=d=AQABBByTsGgCEKYz4tiek5VXeuYqYhRSuH8FEgEBAQHksWi6aFx5yyMA_eMCAA&S=AQAAAh_aWV597HX_B6CpRV6W_JQ; cmp=t=1756402490&j=0&u=1---; gpp=DBAA; gpp_sid=-1; _awl=2.1756402496.5-35f630b61b5391b578689036f67a5ec0-6763652d6575726f70652d7765737431-0; _ga=GA1.1.141835662.1756402527; AS=v=1&s=SG5ze1gk&d=A68b1e612|VWil.oX.2Tp3vjheAtEMVZIR7Ix9PhNbAkETCuz1PaS0At7tBcq9e_EDBF3VQ8Ra5.4I8tC6Tq6UcHmGnw_swvReLSLLGqVLGw6cBoX8rd73qzirWyLJeiSXXLPROo7737SabcnLLIxG8uZPRp8S7zg0wIMet6D4Lt7ZgLGTf4JsZgT_6vFOChFGwMuQl.zbmovQX7FmJF.4NnPApyNlwQTisb9lHBywdDGjAFGM04z5x3Yzxr57ldQ_DRSlwa.qO.wqsgaCEB3TPO0dckvCiNbE96Nj2EpbURCcBIcIrdzqe2KcOnuPwxBdw7VKsTV.B4d4w25x3P8Yo94s.nS.tiwKLwIrGrJOyuKR9C6mr7xCG_MmPNcqup6x2nfqlSLaSZ4bMuQpGkPLo_5dfRFQ7UlZLRAPgG6Q0EMdVHl1X5gPtxo.YA5mIt5MEjSbOjxk8XrfNqhcQQkFc2coj.IOkevNLnoCB2b9UPYMmGc6gjNZlqCFCD.bG4JapmvLJT15rE4ADMYmYEXBK4cIZgsXk0XShS6soUAtcRlGTp2.DNrXiSCzjBzAP.Y1w_KxZU_YheW9B_i6OXKSNcCkk0.TK8_lFxSYzxMoyEJ_IkBZunjhR_EUx3ck_6ANfYghJxxHctgwoAAt0LZBYjDD8cDmAid2Iddu.YZNQ5zgew3otHGhlrlYPjo5PqJIMat44Tsr8aFzm3P4jqavggem3oTQDipw7kQJe6O2Zfv.DxJwFU62tox6g82kDb2HM_6e7oZ5S7YckeT1IOSbsbU9TsmiE_b4l__aJ5f0o5yj6IY91lRWdhOzXVGKRsN3p_u6X9Fbb6VPtjvol8xdZNKV5J09o2vjweyilsqEqXrdDJLNiJAXXqsU.bxqJDtmxhojEAxCv9_AZ_miW9REzOqijCUxm2jc5DwkOWUho5SEZGpjlTNjHMh4Xv3O42peFP09uMas0Z6CAEZKMYIZhPev1y8qm6EkAUKgkQ42GLtiGai_xmpSgRxAcOivWGF5yUOISK12HDa.8dFAY677wrIwd_ApISgwSgxRyfYE_5zGCUud_lHCvrU6_8FrNl3GxCwoTgConWipY73UFCp.6FAQv9OUTCWLwqsE3n8s_N.FkJRhrFn8Ch1gkdePY1mhTQYkDQA15qNlr1Ap5yLmyL6LZ3ZASOR8I.lGZQWmnJ4brt4LsFxtD1o.Uiw161msZwR.4X1oO.Gjh5TVDlVpx6ig8bUYTBMg3b4Hvw--~A|B68b1e59f|F0aZT83.2TraoyWsNVK3vj3REYQmzD.5IqGKyVtCHkkIZ0yxunOVb_yWvC_PRHDSypDIfBY5IK4gtAF3HN8JKRHogG5.CLkDMG922zGtud.t0ofk0j.H33abLKkA_cvHc9OteDjgL4Hpz_hU2epmCZoeGjwWzPUgDk5_p0vBExqay1Y_NjMDgIUxkFi.Xpm9BjSS7M98Z12eZn1QMZF_v71c4AzyI4V2kKpPlDmKOnuGrWdw.hdzULLMXffKX_3ng79hTKHbhjHE0EhT57FnCLztZ2LeqhGge6ZWoef0iyxGmFkOli46ZRtyunfNI9hHgWM4IFVc.tkCoFFpQablh_3iXYzuc5944Jrnv2tj03mtldAnOtQtQdyzMtt_DDkjbzBkBnETirFLuLHbgwEVjzUj7UiLikCXebjQiuRhFe5ID27azWyPF2xVVYiPm9VKLxI6y7BphW8blqrTCnFmfzCEGTxboJorfgpZtX.hdxx8yg6JXfHddDdwCMQJbLsarrydLRJY75.oXrhyBaehem4f5LhNIWRUzi2KeyPWTiHuadBF2vV5TEuiGevOkqC4z8tFXqqm_YN_kVBJkjSXaIpoNPNjQ3CrKmc3kpWAqqHYKdHDs1j2_KC6xgaF_nUc615CNSHsKMX_ZL4qITMnHyJno3HfjGzbgTLtJbyN4WC.lY_2Q0ffdQHgH1mb1GGuTXsJWVmREa7fTC..BAZ9gRXPjIyCAmgz0U8P6Kv78bigfMdURSBIJO49UBTCnv5.O2H03O9ryCeD1IymZ1jJeASg_OXfD4WTCbNKnAklQdnnk.MPUjKXm1doQyH0APOfcXCBSNHJr6y3w3CZgT2AKuW5CcFIzuZe6ZUwtGlu5eOCAQylhES0kPHJIu8BF1TKFYMNKArfl_g6Fa4s.MpmUr9asFh3mxw585sfcZjLv0Q06TIVs8JIPUlTrPpN_ZFoA3BjATTqPR0dRerhbXjkPl_4OSqzKqPMv5yYYuAjac7jITZWu3SsGsscezqeWCVreC.QLrGR5XApCn.BeX1uN83bvF3ye__P30jRZvwIKNbDlq45IrysN1wHjBUVeL_UBpyLVQ1s.AJnGboDXYPkrKI8hVrR3ZlIl78mkDDVlt9EWXG2Ryvf00MtnkWrrXRnmdjbDFjcgOo1MDdX570iIHnrlqfEp1WhSdN0FzcFjRIEHUWjRHFZqChwFFJulcvv62e6yPOzJyIsb3UW635yccEWaEWBOIU-~A; _ga_7XMXL3P19Q=GS2.1.s1756402525$o1$g1$t1756402849$j60$l0$h0',
			    'origin': 'https://login.aol.com',
			    'referer': 'https://login.aol.com/account/create?lang=en-US&src=mail&activity=mail-direct&pspid=972825001&done=https%3A%2F%2Fapi.login.aol.com%2Foauth2%2Fauthorize%3Factivity%3Dmail-direct%26client_id%3Ddj0yJmk9VlN3cDhpNm1Id0szJmQ9WVdrOVdtRm1aMVU1Tm1zbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmeD1mYQ--%26language%3Den-US%26nonce%3Dqa0CRt58S4AXAjJQBBx0zTFYWFCUfTqr%26pspid%3D972825001%26redirect_uri%3Dhttps%253A%252F%252Foidc.mail.aol.com%252Fcallback%26response_type%3Dcode%26scope%3Dmail-r%2Bycal-w%2Bopenid%2Bopenid2%2Bmail-w%2Bmail-x%2Bsdps-r%2Bmsgr-w%26src%3Dmail%26state%3DeyJhbGciOiJSUzI1NiIsImtpZCI6IjZmZjk0Y2RhZDExZTdjM2FjMDhkYzllYzNjNDQ4NDRiODdlMzY0ZjcifQ.eyJyZWRpcmVjdFVyaSI6Imh0dHBzOi8vbWFpbC5hb2wuY29tL2QifQ.JMX40ZssLtCMlaqAOZYFU6Tz6rggXd8IYA-lVO2jkmWcFPGEJ3tTkOj7qGkKjtTLXofPUFFQ6Uzih1pYCkh_fgS1zD8X5Ge3c0oSKTchP4AdNmsEetEyDMoUijvOWJVVbDe0byUHYQzCmE7F-o2187M5fpzxgGEV6U-7Xm4ywaA&specId=yidregsimplified',
			    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
			    'sec-ch-ua-mobile': '?0',
			    'sec-ch-ua-platform': '"Linux"',
			    'sec-fetch-dest': 'empty',
			    'sec-fetch-mode': 'cors',
			    'sec-fetch-site': 'same-origin',
			    'user-agent': str(generate_user_agent()),
			    'x-requested-with': 'XMLHttpRequest',
			}
			
			params = {
			    'validateField': 'userId',
			}
			
			data = f'browser-fp-data=%7B%22language%22%3A%22ar-EG%22%2C%22colorDepth%22%3A24%2C%22deviceMemory%22%3A8%2C%22pixelRatio%22%3A3.0234789848327637%2C%22hardwareConcurrency%22%3A8%2C%22timezoneOffset%22%3A-180%2C%22timezone%22%3A%22Asia%2FBaghdad%22%2C%22sessionStorage%22%3A1%2C%22localStorage%22%3A1%2C%22indexedDb%22%3A1%2C%22openDatabase%22%3A1%2C%22cpuClass%22%3A%22unknown%22%2C%22platform%22%3A%22Linux%20armv81%22%2C%22doNotTrack%22%3A%22unknown%22%2C%22plugins%22%3A%7B%22count%22%3A0%2C%22hash%22%3A%2224700f9f1986800ab4fcc880530dd0ed%22%7D%2C%22canvas%22%3A%22canvas%20winding%3Ayes~canvas%22%2C%22webgl%22%3A1%2C%22webglVendorAndRenderer%22%3A%22Google%20Inc.%20(Qualcomm)~ANGLE%20(Qualcomm%2C%20Adreno%20(TM)%20619%2C%20OpenGL%20ES%203.2)%22%2C%22adBlock%22%3A0%2C%22hasLiedLanguages%22%3A0%2C%22hasLiedResolution%22%3A0%2C%22hasLiedOs%22%3A1%2C%22hasLiedBrowser%22%3A0%2C%22touchSupport%22%3A%7B%22points%22%3A5%2C%22event%22%3A1%2C%22start%22%3A1%7D%2C%22fonts%22%3A%7B%22count%22%3A7%2C%22hash%22%3A%225cbe5386d7eb568c82e66c0c19fe9071%22%7D%2C%22audio%22%3A%22124.08072766105033%22%2C%22resolution%22%3A%7B%22w%22%3A%22393%22%2C%22h%22%3A%22873%22%7D%2C%22availableResolution%22%3A%7B%22w%22%3A%22873%22%2C%22h%22%3A%22393%22%7D%2C%22ts%22%3A%7B%22serve%22%3A1756402834543%2C%22render%22%3A1756402835104%7D%7D&specId=yidregsimplified&context=REGISTRATION&cacheStored=&crumb=Kqwkzo3EMKeHJ0tUQqtyw&acrumb=SG5ze1gk&sessionIndex=QQ--&done=https%3A%2F%2Fapi.login.aol.com%2Foauth2%2Fauthorize%3Factivity%3Dmail-direct%26client_id%3Ddj0yJmk9VlN3cDhpNm1Id0szJmQ9WVdrOVdtRm1aMVU1Tm1zbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmeD1mYQ--%26language%3Den-US%26nonce%3Dqa0CRt58S4AXAjJQBBx0zTFYWFCUfTqr%26pspid%3D972825001%26redirect_uri%3Dhttps%253A%252F%252Foidc.mail.aol.com%252Fcallback%26response_type%3Dcode%26scope%3Dmail-r%2Bycal-w%2Bopenid%2Bopenid2%2Bmail-w%2Bmail-x%2Bsdps-r%2Bmsgr-w%26src%3Dmail%26state%3DeyJhbGciOiJSUzI1NiIsImtpZCI6IjZmZjk0Y2RhZDExZTdjM2FjMDhkYzllYzNjNDQ4NDRiODdlMzY0ZjcifQ.eyJyZWRpcmVjdFVyaSI6Imh0dHBzOi8vbWFpbC5hb2wuY29tL2QifQ.JMX40ZssLtCMlaqAOZYFU6Tz6rggXd8IYA-lVO2jkmWcFPGEJ3tTkOj7qGkKjtTLXofPUFFQ6Uzih1pYCkh_fgS1zD8X5Ge3c0oSKTchP4AdNmsEetEyDMoUijvOWJVVbDe0byUHYQzCmE7F-o2187M5fpzxgGEV6U-7Xm4ywaA&googleIdToken=&authCode=&attrSetIndex=0&specData=&deviceCapability=%7B%22pa%22%3A%7B%22status%22%3Afalse%7D%2C%22isWebAuthnSupported%22%3Atrue%7D&tos0=oath_freereg%7Cus%7Cen-US&multiDomain=&asId=7e90c42f-503b-444a-8f5c-8c8a5b1d3f66&fingerprintCaptured=&firstName=Atro&lastName=Hdhdh&userid-domain=yahoo&userId={email}&password=law20005%403gsb&mm=9&dd=1&yyyy=2000&signup='
			
			response = requests.post('https://login.aol.com/account/module/create', params=params, cookies=cookies, headers=headers, data=data).text
			
			if '"errors":[]' in response:
				print(f'GOOD AOL : {email}')
				
				cookies = {
				    'ig_did': 'C5000B14-C007-4297-931D-988B622F5426',
				    'datr': 'L0h4aHX-XpN43taBi2bCfZ-B',
				    'ig_nrcb': '1',
				    'mid': 'aHhILwABAAFJkpRVlAEioZBcPfhc',
				    'ps_l': '1',
				    'ps_n': '1',
				    'dpr': '3.0234789848327637',
				    'csrftoken': 'FpVUS77tTdF3iU99uAHLtmFMpm6YI6Xo',
				    'wd': '891x1671',
				}
				
				headers = {
				    'authority': 'www.instagram.com',
				    'accept': '*/*',
				    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
				    # 'cookie': 'ig_did=C5000B14-C007-4297-931D-988B622F5426; datr=L0h4aHX-XpN43taBi2bCfZ-B; ig_nrcb=1; mid=aHhILwABAAFJkpRVlAEioZBcPfhc; ps_l=1; ps_n=1; dpr=3.0234789848327637; csrftoken=FpVUS77tTdF3iU99uAHLtmFMpm6YI6Xo; wd=891x1671',
				    'referer': 'https://www.instagram.com/dfff/',
				    'sec-ch-prefers-color-scheme': 'dark',
				    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
				    'sec-ch-ua-full-version-list': '"Chromium";v="137.0.7337.0", "Not/A)Brand";v="24.0.0.0"',
				    'sec-ch-ua-mobile': '?0',
				    'sec-ch-ua-model': '""',
				    'sec-ch-ua-platform': '"Linux"',
				    'sec-ch-ua-platform-version': '""',
				    'sec-fetch-dest': 'empty',
				    'sec-fetch-mode': 'cors',
				    'sec-fetch-site': 'same-origin',
				    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
				    'x-asbd-id': '359341',
				    'x-csrftoken': 'FpVUS77tTdF3iU99uAHLtmFMpm6YI6Xo',
				    'x-ig-app-id': '936619743392459',
				    'x-ig-www-claim': '0',
				    'x-requested-with': 'XMLHttpRequest',
				    'x-web-session-id': 'dbdh88:ixktcq:eabyqw',
				}
				
				params = {
				    'username': email,
				}
				try:
				    response = requests.get(
				    'https://www.instagram.com/api/v1/users/web_profile_info/',
				    params=params,
				    cookies=cookies,
				    headers=headers,
				).json()
				except json.decoder.JSONDecodeError:
					continue
					
				io = response['data']['user'][ 'biography']
				fol = response['data']['user']['edge_followed_by']['count']
				fos = response['data']['user']['edge_follow']['count']
				ido = response['data']['user']['id']
				nam = response['data']['user']['full_name']
				isp = response['data']['user']['is_private']
				op = response['data']['user']['edge_owner_to_timeline_media']['count']
				ff = f'''
				╔══✪〘
									𝐈𝐍𝐅𝐎𝐑𝐌𝐀𝐓𝐈𝐎𝐍 〙✪══╗
				[*] NAME
				{nam}
				[*] USER        : {email}
				[*] EMAIL       : {email}
				[*] FOLLOWERS   : {fol}
				[*] FOLLOWING   : {fos}
				[*] ID          : {ido}
				[*] POSTS       : {op}
				[*] LINK        : https://www.instagram.com/{email}
									╚═══════✪〘 BY : @S_O_F3 〙✪═══════╝
				'''
				print(ff)
				tlg = (f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={ff}')
				i = requests.post(tlg)				
				
				
				
				
			else:
				print(f'BAD AOL : {email}')
			
			
			
		else:
			print(f'BAD INS : {email}')
			
ss()