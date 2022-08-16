# 로봇 청소기

import sys

sys.stdin = open("input.txt","r")
input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d =  map(int, input().split())
map = [list(map(int, input().split())) for _ in range(N)]

