def GreedySorting(p: list[str]) -> list[list[str]]:
    p_sequence = []
    for i in range(len(p)):
        val_index =i+1
        index, is_positive = findIndex(p, i+1)
        val = "+"+str(i) if is_positive else "-"+str(i)
        if index != i:
            p[i:index+1] = reversal(p[i:index+1])
            p_sequence.append(" ".join(p))
        if isPositive(p[i]):
            p[i] = "+"+p[i][1:]
            p_sequence.append(" ".join(p))
    return p_sequence


def findIndex(p: list[str], k: int) -> tuple[int, bool]:
    for i in range(len(p)):
        if abs(int(p[i])) == k:
            return i, int(p[i]) > 0
    
def reversal(p: list[str]):
    reversed_p = list(reversed(p))
    for i in range(len(reversed_p)):
        reversed_p[i] = switchSigns(reversed_p[i])
    return reversed_p

def switchSigns(s: str) -> str:
    if not isPositive(s):
        return "+"+s[1:]
    return "-"+s[1:]

def isPositive(s: str) -> bool:
    return s[0] == "+"

if __name__ == "__main__":
    p_str = "-340 -324 +233 -345 +21 +120 -366 -419 +105 -25 +356 -148 +279 +59 -110 +231 -375 +330 +199 +48 +122 -42 +236 -365 -26 +275 -60 -227 +259 -338 +183 -126 -223 -354 +93 -288 -221 -332 +219 +400 -350 +147 -286 +143 +161 -213 -234 -152 -17 -109 -116 -176 +131 -55 +323 +267 +285 +82 +287 -61 -207 -83 -1 -7 -188 +242 -78 -396 -392 +274 -258 -371 -309 +69 +45 +57 +314 +228 +373 -90 +159 +348 -239 -257 -136 -63 -144 +162 +104 +278 +406 +182 -170 -158 -169 +265 +399 +226 -201 +33 -79 +357 -118 +212 -343 +196 -154 +326 -89 +187 -291 -269 -240 +115 +405 -130 +195 +386 +310 +281 +420 +85 +172 +128 -16 +49 +404 -304 +376 +331 +168 +73 +282 +124 +302 -232 +121 +398 +355 -74 +146 -247 +165 -75 +362 +5 -395 -253 +41 -316 -205 -56 -24 -37 -262 +150 -250 -409 +283 -290 -64 +10 +378 -211 -43 -51 -65 -370 +235 -35 -377 -84 -353 -40 -34 -103 +125 +28 -422 +209 -335 +108 +294 +328 +6 +417 +38 -29 +36 -284 +206 +296 +300 -100 -312 -237 +166 -76 -384 -244 -208 +245 +397 -140 -401 +119 +261 +299 +292 +347 +194 +80 -62 +117 +9 +238 +214 +382 +321 +71 +307 +252 -218 +190 -308 -3 -98 +30 +361 +171 +341 -106 +295 +298 +352 +418 -13 -413 -387 -129 -351 -254 -319 -58 -318 -94 +315 +177 -87 -317 +391 +181 -180 +416 -132 +402 -163 +151 -408 +97 +142 -77 +46 +67 -27 -342 -364 -173 -210 +134 -388 -349 -359 +368 -276 +91 -339 +92 -264 +255 +193 -11 +385 +263 +230 -191 +241 -225 +268 -320 +272 -149 -81 -31 -139 -337 +164 -204 +19 -403 -123 -222 +289 +360 -306 -367 +248 +23 +39 +380 -260 +135 -224 -22 -107 -383 -246 -12 -369 +297 -344 -99 -305 -280 +44 -412 +113 -167 -156 +145 -336 -325 -101 +203 +53 +47 +50 +389 +293 +8 -137 +410 +346 -220 +186 -256 +249 +215 +153 +311 +141 -127 -72 -138 +411 -421 -390 -303 -358 -216 +192 -266 +333 +313 -277 -270 -32 -102 -189 -2 -68 -414 +329 -334 -271 -198 -114 -174 +393 -155 -327 -175 -273 +70 +95 +217 -301 -4 +52 -88 -18 +229 -54 -415 +184 +200 -363 -243 +202 -112 -251 -379 +178 -179 -157 +197 -160 +185 -381 -96 +372 -374 -15 +133 -111 -394 +20 -407 +14 +322 -86 +66"
    path = "./datasets/dataset_286_4.txt"
    with open(path) as f:
        p_str = f.readline().strip()
    p = p_str.strip().split(" ")
    result = GreedySorting(p)
    with open('./results/greedy_sorting.txt', 'w') as f:
        f.write("\n".join(result))
