# ContextC++?

ContextC++の実装プロトタイプです．

入力例はccpp1.hlで，以下のようになっています:
```
@layers = [base, l1]

class CCpp1
{
public:
    @base int calc (int a, int b);
};
```
@layersで使用するレイヤの定義を行い，@baseでレイヤで変更されうる関数の指定をします．

これを

```
python croscpp.py ccpp1.hl
```

とすると，ccpp1.h，ccpp1_gen.cppが生成されます．

これらとccpp1.cppを組み合わせると，コンテキスト指向プログラミングの実装を体験できます．
