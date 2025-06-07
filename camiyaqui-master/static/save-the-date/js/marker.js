google.maps.__gjsload__('marker', function (_) {
    var IQ, JQ, KQ, LQ, MQ, NQ, PQ, SQ, QQ, TQ, RQ, XQ, YQ, VQ, ZQ, aR, dR, bR, eR, gR, fR, hR, iR, jR, kR, tR, lR, qR,
        oR, rR, mR, pR, uR, nR, sR, GR, yR, zR, AR, BR, CR, DR, ER, FR, IR, JR, xR, LR, KR, MR, OR, NR, PR, RR, QR, SR,
        VR, UR, TR, WR, XR, YR, $R, ZR, bS, aS, eS, fS, gS, dS, cS, jS, iS, hS, kS, lS;
    IQ = function (a) {
        var b = 1;
        return function () {
            --b || a()
        }
    };
    JQ = function (a, b) {
        _.sv().Ba.load(new _.UA(a), function (a) {
            b(a && a.size)
        })
    };
    KQ = function (a) {
        this.l = a;
        this.j = !1
    };
    LQ = function (a, b) {
        if (!b) return null;
        var c = a.get("snappingCallback");
        c && (b = c(b));
        c = b.x;
        b = b.y;
        var d = a.get("referencePosition");
        d && (2 == a.l ? c = d.x : 1 == a.l && (b = d.y));
        return new _.N(c, b)
    };
    window.Animation = function (a) {
        this.j = a;
        this.l = ""
    };
    MQ = function (a, b) {
        var c = [];
        c.push("@-webkit-keyframes ", b, " {\n");
        _.D(a.j, function (a) {
            c.push(100 * a.time + "% { ");
            c.push("-webkit-transform: translate3d(" + a.translate[0] + "px,", a.translate[1] + "px,0); ");
            c.push("-webkit-animation-timing-function: ", a.ib, "; ");
            c.push("}\n")
        });
        c.push("}\n");
        return c.join("")
    };
    NQ = function (a, b) {
        for (var c = 0; c < a.j.length - 1; c++) {
            var d = a.j[c + 1];
            if (b >= a.j[c].time && b < d.time) return c
        }
        return a.j.length - 1
    };
    PQ = function (a) {
        if (a.l) return a.l;
        a.l = "_gm" + Math.round(1E4 * Math.random());
        var b = MQ(a, a.l);
        if (!OQ) {
            OQ = _.Rb("style");
            OQ.type = "text/css";
            var c = window.document;
            c = c.querySelectorAll && c.querySelector ? c.querySelectorAll("HEAD") : c.getElementsByTagName("HEAD");
            c[0].appendChild(OQ)
        }
        OQ.textContent += b;
        return a.l
    };
    SQ = function (a, b, c) {
        var d, e;
        if (e = 0 != c.ti) e = 5 == _.Bi.l.j || 6 == _.Bi.l.j || 3 == _.Bi.l.type && _.Jj(_.Bi.l.version, 7);
        e ? d = new QQ(a, b, c) : d = new RQ(a, b, c);
        d.start();
        return d
    };
    QQ = function (a, b, c) {
        this.sa = a;
        this.m = b;
        this.j = c;
        this.l = !1
    };
    TQ = function (a, b, c) {
        _.xk(function () {
            a.style.WebkitAnimationDuration = c.duration ? c.duration + "ms" : null;
            a.style.WebkitAnimationIterationCount = c.Xb;
            a.style.WebkitAnimationName = b
        })
    };
    RQ = function (a, b, c) {
        this.sa = a;
        this.A = b;
        this.l = -1;
        "infinity" != c.Xb && (this.l = c.Xb || 1);
        this.B = c.duration || 1E3;
        this.j = !1;
        this.m = 0
    };
    XQ = function () {
        for (var a = [], b = 0; b < UQ.length; b++) {
            var c = UQ[b];
            VQ(c);
            c.j || a.push(c)
        }
        UQ = a;
        0 == UQ.length && (window.clearInterval(WQ), WQ = null)
    };
    YQ = function (a) {
        return a ? a.__gm_at || _.vi : null
    };
    VQ = function (a) {
        if (!a.j) {
            var b = _.vk();
            ZQ(a, (b - a.m) / a.B);
            b >= a.m + a.B && (a.m = _.vk(), "infinite" != a.l && (a.l--, a.l || a.cancel()))
        }
    };
    ZQ = function (a, b) {
        var c = 1, d = a.A;
        var e = d.j[NQ(d, b)];
        var f;
        d = a.A;
        (f = d.j[NQ(d, b) + 1]) && (c = (b - e.time) / (f.time - e.time));
        b = YQ(a.sa);
        d = a.sa;
        f ? (c = (0, $Q[e.ib || "linear"])(c), e = e.translate, f = f.translate, c = new _.N(Math.round(c * f[0] - c * e[0] + e[0]), Math.round(c * f[1] - c * e[1] + e[1]))) : c = new _.N(e.translate[0], e.translate[1]);
        c = d.__gm_at = c;
        d = c.x - b.x;
        b = c.y - b.y;
        if (0 != d || 0 != b) c = a.sa, e = new _.N(_.uk(c.style.left) || 0, _.uk(c.style.top) || 0), e.x = e.x + d, e.y += b, _.Nk(c, e);
        _.R.trigger(a, "tick")
    };
    aR = function () {
        var a = _.Sv();
        this.icon = a ? {
            url: _.$l("api-3/images/spotlight-poi2", !0),
            scaledSize: new _.O(27, 43),
            origin: new _.N(0, 0),
            anchor: new _.N(14, 43),
            labelOrigin: new _.N(14, 15)
        } : {
            url: _.$l("api-3/images/spotlight-poi", !0),
            scaledSize: new _.O(22, 40),
            origin: new _.N(0, 0),
            anchor: new _.N(11, 40),
            labelOrigin: new _.N(11, 12)
        };
        this.l = a ? {
            url: _.$l("api-3/images/spotlight-poi-dotless2", !0),
            scaledSize: new _.O(27, 43),
            origin: new _.N(0, 0),
            anchor: new _.N(14, 43),
            labelOrigin: new _.N(14, 15)
        } : {
            url: _.$l("api-3/images/spotlight-poi-dotless",
                !0),
            scaledSize: new _.O(22, 40),
            origin: new _.N(0, 0),
            anchor: new _.N(11, 40),
            labelOrigin: new _.N(11, 12)
        };
        this.j = a ? {
            url: _.$l("api-3/images/drag-cross", !0),
            scaledSize: new _.O(13, 11),
            origin: new _.N(0, 0),
            anchor: new _.N(7, 6)
        } : {
            url: _.aw("icons/spotlight/directions_drag_cross_67_16.png", 4),
            size: new _.O(16, 16),
            origin: new _.N(0, 0),
            anchor: new _.N(8, 8)
        };
        this.shape = a ? {coords: [13.5, 0, 4, 3.75, 0, 13.5, 13.5, 43, 27, 13.5, 23, 3.75], type: "poly"} : {
            coords: [8, 0, 5, 1, 4, 2, 3, 3, 2, 4, 2, 5, 1, 6, 1, 7, 0, 8, 0, 14, 1, 15, 1, 16, 2, 17, 2, 18, 3, 19, 3, 20,
                4, 21, 5, 22, 5, 23, 6, 24, 7, 25, 7, 27, 8, 28, 8, 29, 9, 30, 9, 33, 10, 34, 10, 40, 11, 40, 11, 34, 12, 33, 12, 30, 13, 29, 13, 28, 14, 27, 14, 25, 15, 24, 16, 23, 16, 22, 17, 21, 18, 20, 18, 19, 19, 18, 19, 17, 20, 16, 20, 15, 21, 14, 21, 8, 20, 7, 20, 6, 19, 5, 19, 4, 18, 3, 17, 2, 16, 1, 14, 1, 13, 0, 8, 0],
            type: "poly"
        }
    };
    dR = function (a) {
        var b = this;
        this.j = a;
        this.T = new _.gg(function () {
            var a = b.get("modelIcon"), d = b.get("modelLabel");
            bR(b, "viewIcon", a || d && cR.l || cR.icon);
            bR(b, "viewCross", cR.j);
            d = b.get("useDefaults");
            var e = b.get("modelShape");
            e || a && !d || (e = cR.shape);
            b.get("viewShape") != e && b.set("viewShape", e)
        }, 0);
        cR || (cR = new aR)
    };
    bR = function (a, b, c) {
        eR(a, c, function (c) {
            a.set(b, c);
            c = a.get("modelLabel");
            a.set("viewLabel", c ? {
                text: c.text || c,
                color: _.Bc(c.color, "#000000"),
                fontWeight: _.Bc(c.fontWeight, ""),
                fontSize: _.Bc(c.fontSize, "14px"),
                fontFamily: _.Bc(c.fontFamily, "Roboto,Arial,sans-serif")
            } : null)
        })
    };
    eR = function (a, b, c) {
        b ? null != b.path ? c(a.j(b)) : (_.Ec(b) || (b.size = b.size || b.scaledSize), b.size ? c(b) : (b.url || (b = {url: b}), JQ(b.url, function (a) {
            b.size = a || new _.O(24, 24);
            c(b)
        }))) : c(null)
    };
    gR = function () {
        this.j = fR(this);
        this.set("shouldRender", this.j);
        this.l = !1
    };
    fR = function (a) {
        var b = a.get("mapPixelBoundsQ"), c = a.get("icon"), d = a.get("position");
        if (!b || !c || !d) return 0 != a.get("visible");
        var e = c.anchor || _.vi, f = c.size.width + Math.abs(e.x);
        c = c.size.height + Math.abs(e.y);
        return d.x > b.U - f && d.y > b.W - c && d.x < b.Y + f && d.y < b.Z + c ? 0 != a.get("visible") : !1
    };
    hR = function (a) {
        this.l = a;
        this.j = !1
    };
    iR = function (a, b, c, d) {
        this.B = c;
        this.m = a;
        this.A = b;
        this.C = d;
        this.D = 0;
        this.l = null;
        this.j = new _.gg(this.Qi, 0, this)
    };
    jR = function (a, b) {
        a.pa = b;
        _.hg(a.j)
    };
    kR = function (a) {
        a.l && (_.Hk(a.l), a.l = null)
    };
    tR = function (a, b) {
        var c = this;
        this.T = new _.gg(function () {
            var a = c.get("panes"), b = c.get("scale");
            if (!a || !c.getPosition() || 0 == c.Ri() || _.L(b) && .1 > b && !c.get("dragging")) lR(c); else {
                var f = a.markerLayer;
                if (b = c.vf()) {
                    var g = null != b.url;
                    c.j && c.Hc == g && (_.Hk(c.j), c.j = null);
                    c.Hc = !g;
                    c.j = mR(c, f, c.j, b);
                    f = nR(c);
                    g = b.size;
                    c.Sb.width = f * g.width;
                    c.Sb.height = f * g.height;
                    c.set("size", c.Sb);
                    var h = c.get("anchorPoint");
                    if (!h || h.j) b = b.anchor, c.la.x = f * (b ? g.width / 2 - b.x : 0), c.la.y = -f * (b ? b.y : g.height), c.la.j = !0, c.set("anchorPoint", c.la)
                }
                if (!c.da &&
                    (g = c.vf()) && (b = 0 != c.get("clickable"), f = c.getDraggable(), b || f)) {
                    h = g.url || _.hr;
                    var k = null != g.url, m = {};
                    if (_.Gk()) {
                        k = g.size.width;
                        var p = g.size.height, q = new _.O(k + 16, p + 16);
                        g = {
                            url: h,
                            size: q,
                            anchor: g.anchor ? new _.N(g.anchor.x + 8, g.anchor.y + 8) : new _.N(Math.round(k / 2) + 8, p + 8),
                            scaledSize: q
                        }
                    } else if (_.je.l || _.je.m) if (m.shape = c.get("shape"), m.shape || !k) k = g.scaledSize || g.size, g = {
                        url: h,
                        size: k,
                        anchor: g.anchor,
                        scaledSize: k
                    };
                    k = null != g.url;
                    c.Jc == k && oR(c);
                    c.Jc = !k;
                    g = c.C = mR(c, c.getPanes().overlayMouseTarget, c.C, g, m);
                    _.Ev(g,
                        0);
                    h = g;
                    if ((m = h.getAttribute("usemap") || h.firstChild && h.firstChild.getAttribute("usemap")) && m.length && (h = _.Ik(h).getElementById(m.substr(1)))) var t = h.firstChild;
                    g = t || g;
                    g.title = c.get("title") || "";
                    f && !c.B && (t = c.B = new _.$B(g, c.Rb, c.C), c.Rb ? (t.bindTo("deltaClientPosition", c), t.bindTo("position", c)) : t.bindTo("position", c.yb, "rawPosition"), t.bindTo("containerPixelBounds", c, "mapPixelBounds"), t.bindTo("anchorPoint", c), t.bindTo("size", c), t.bindTo("panningEnabled", c), t && !c.Ga && (c.Ga = [_.R.forward(t, "dragstart",
                        c), _.R.forward(t, "drag", c), _.R.forward(t, "dragend", c), _.R.forward(t, "panbynow", c)]));
                    t = c.get("cursor") || "pointer";
                    f ? c.B.set("draggableCursor", t) : _.Dv(g, b ? t : "");
                    pR(c, g)
                }
                a = a.overlayLayer;
                if (b = t = c.get("cross")) b = c.get("crossOnDrag"), _.r(b) || (b = c.get("raiseOnDrag")), b = 0 != b && c.getDraggable() && c.get("dragging");
                b ? c.m = mR(c, a, c.m, t) : (c.m && _.Hk(c.m), c.m = null);
                c.D = [c.j, c.m, c.C];
                qR(c);
                for (a = 0; a < c.D.length; ++a) if (b = c.D[a]) t = b, f = b.j, g = YQ(b) || _.vi, b = nR(c), f = rR(c, f, b, g), _.Nk(t, f), (f = _.Bi.j) && (t.style[f] = 1 != b ? "scale(" +
                    b + ") " : ""), b = c.get("zIndex"), c.get("dragging") && (b = 1E6), _.L(b) || (b = Math.min(c.getPosition().y, 999999)), _.Ok(t, b), c.A && c.A.setZIndex(b);
                sR(c);
                for (a = 0; a < c.D.length; ++a) (t = c.D[a]) && _.Bv(t)
            }
        }, 0);
        this.Ud = a;
        this.Rb = b || !1;
        this.yb = new KQ(0);
        this.yb.bindTo("position", this);
        this.A = this.j = null;
        this.sd = [];
        this.Hc = !1;
        this.C = null;
        this.Jc = !1;
        this.m = null;
        this.D = [];
        this.gc = new _.N(0, 0);
        this.Sb = new _.O(0, 0);
        this.la = new _.N(0, 0);
        this.Tb = !0;
        this.da = 0;
        this.l = this.Ic = this.ud = this.td = null;
        this.fc = !1;
        this.Gc = [_.R.addListener(this,
            "dragstart", this.Ti), _.R.addListener(this, "dragend", this.Si), _.R.addListener(this, "panbynow", function () {
            return c.T.Ma()
        })];
        this.sa = this.I = this.G = this.B = this.K = this.Ga = null
    };
    lR = function (a) {
        a.A && (uR(a.sd), a.A.release(), a.A = null);
        a.j && _.Hk(a.j);
        a.j = null;
        a.m && _.Hk(a.m);
        a.m = null;
        oR(a);
        a.D = []
    };
    qR = function (a) {
        var b = a.ck();
        if (b) {
            if (!a.A) {
                var c = a.A = new iR(a.getPanes(), b, a.get("opacity"), a.get("visible"));
                a.sd = [_.R.addListener(a, "label_changed", function () {
                    c.setLabel(this.get("label"))
                }), _.R.addListener(a, "opacity_changed", function () {
                    c.setOpacity(this.get("opacity"))
                }), _.R.addListener(a, "panes_changed", function () {
                    var a = this.get("panes");
                    c.m = a;
                    kR(c);
                    _.hg(c.j)
                }), _.R.addListener(a, "visible_changed", function () {
                    c.setVisible(this.get("visible"))
                })]
            }
            b = a.vf();
            a.getPosition();
            if (b) {
                var d = a.j, e = nR(a);
                d = rR(a, b, e, YQ(d) || _.vi);
                b = b.labelOrigin || new _.N(b.size.width / 2, b.size.height / 2);
                jR(a.A, new _.N(d.x + b.x, d.y + b.y));
                a.A.j.Ma()
            }
        }
    };
    oR = function (a) {
        a.da ? a.fc = !0 : (a.C && _.Hk(a.C), a.C = null, a.B && (a.B.unbindAll(), a.B.release(), a.B = null, uR(a.Ga), a.Ga = null), a.G && a.G.remove(), a.I && a.I.remove())
    };
    rR = function (a, b, c, d) {
        var e = a.getPosition(), f = b.size, g = (b = b.anchor) ? b.x : f.width / 2;
        a.gc.x = e.x + d.x - Math.round(g - (g - f.width / 2) * (1 - c));
        b = b ? b.y : f.height;
        a.gc.y = e.y + d.y - Math.round(b - (b - f.height / 2) * (1 - c));
        return a.gc
    };
    mR = function (a, b, c, d, e) {
        if (null != d.url) {
            var f = e;
            e = d.origin || _.vi;
            var g = a.get("opacity");
            a = _.Bc(g, 1);
            c ? (c.firstChild.__src__ != d.url && (b = c.firstChild, _.lB(b, d.url, b.A)), _.pB(c, d.size, e, d.scaledSize), c.firstChild.style.opacity = a) : (f = f || {}, f.l = 1 != _.je.type, f.alpha = !0, f.opacity = g, c = _.oB(d.url, null, e, d.size, null, d.scaledSize, f), _.Av(c), b.appendChild(c));
            a = c
        } else b = c || _.X("div", b), vR(b, d), c = b, a = a.get("opacity"), _.Ev(c, _.Bc(a, 1)), a = b;
        c = a;
        c.j = d;
        return c
    };
    pR = function (a, b) {
        a.G && a.I && a.sa == b || (a.sa = b, a.G && a.G.remove(), a.I && a.I.remove(), a.G = _.Fn(b, {
            Ia: function (b) {
                a.da++;
                _.Um(b);
                _.R.trigger(a, "mousedown", b.ea)
            }, La: function (b) {
                a.da--;
                !a.da && a.fc && _.tv(this, function () {
                    a.fc = !1;
                    oR(a);
                    a.T.Ma()
                }, 0);
                _.Wm(b);
                _.R.trigger(a, "mouseup", b.ea)
            }, gb: function (b) {
                var c = b.event;
                b = b.qc;
                _.Xm(c);
                3 == c.button ? b || _.R.trigger(a, "rightclick", c.ea) : b ? _.R.trigger(a, "dblclick", c.ea) : _.R.trigger(a, "click", c.ea)
            }
        }), a.I = new _.uq(b, b, {
            Jd: function (b) {
                _.R.trigger(a, "mouseout", b)
            }, Kd: function (b) {
                _.R.trigger(a,
                    "mouseover", b)
            }
        }))
    };
    uR = function (a) {
        if (a) for (var b = 0, c = a.length; b < c; b++) _.R.removeListener(a[b])
    };
    nR = function (a) {
        return _.Bi.j ? Math.min(1, a.get("scale") || 1) : 1
    };
    sR = function (a) {
        if (!a.Tb) {
            a.l && (a.K && _.R.removeListener(a.K), a.l.cancel(), a.l = null);
            var b = a.get("animation");
            if (b = wR[b]) {
                var c = b.options;
                a.j && (a.Tb = !0, a.set("animating", !0), b = SQ(a.j, b.icon, c), a.l = b, a.K = _.R.addListenerOnce(b, "done", function () {
                    a.set("animating", !1);
                    a.l = null;
                    a.set("animation", null)
                }))
            }
        }
    };
    GR = function (a, b, c, d, e) {
        var f = this;
        this.Ka = b;
        this.j = a;
        this.da = e;
        this.G = b instanceof _.ce;
        a = xR(this);
        b = this.G && a ? _.ml(a, b.getProjection()) : null;
        this.l = new tR(d, !!this.G);
        this.I = !0;
        this.K = this.ia = null;
        (this.m = this.G ? new _.Ov(e.l, this.l, b, e, function () {
            if (f.l.get("dragging") && !f.j.get("place")) {
                var a = f.m.getPosition();
                a && (a = _.nl(a, f.Ka.get("projection")), f.I = !1, f.j.set("position", a), f.I = !0)
            }
        }) : null) && e.ra(this.m);
        this.A = new dR(c);
        this.ca = this.G ? null : new _.HB;
        this.C = this.G ? null : new gR;
        this.D = new _.S;
        this.D.bindTo("position",
            this.j);
        this.D.bindTo("place", this.j);
        this.D.bindTo("draggable", this.j);
        this.D.bindTo("dragging", this.j);
        this.A.bindTo("modelIcon", this.j, "icon");
        this.A.bindTo("modelLabel", this.j, "label");
        this.A.bindTo("modelCross", this.j, "cross");
        this.A.bindTo("modelShape", this.j, "shape");
        this.A.bindTo("useDefaults", this.j, "useDefaults");
        this.l.bindTo("icon", this.A, "viewIcon");
        this.l.bindTo("label", this.A, "viewLabel");
        this.l.bindTo("cross", this.A, "viewCross");
        this.l.bindTo("shape", this.A, "viewShape");
        this.l.bindTo("title",
            this.j);
        this.l.bindTo("cursor", this.j);
        this.l.bindTo("dragging", this.j);
        this.l.bindTo("clickable", this.j);
        this.l.bindTo("zIndex", this.j);
        this.l.bindTo("opacity", this.j);
        this.l.bindTo("anchorPoint", this.j);
        this.l.bindTo("animation", this.j);
        this.l.bindTo("crossOnDrag", this.j);
        this.l.bindTo("raiseOnDrag", this.j);
        this.l.bindTo("animating", this.j);
        this.C || this.l.bindTo("visible", this.j);
        yR(this);
        zR(this);
        this.B = [];
        AR(this);
        this.G ? (BR(this), CR(this), DR(this)) : (ER(this), this.ca && (this.C.bindTo("visible",
            this.j), this.C.bindTo("cursor", this.j), this.C.bindTo("icon", this.j), this.C.bindTo("icon", this.A, "viewIcon"), this.C.bindTo("mapPixelBoundsQ", this.Ka.__gm, "pixelBoundsQ"), this.C.bindTo("position", this.ca, "pixelPosition"), this.l.bindTo("visible", this.C, "shouldRender")), FR(this))
    };
    yR = function (a) {
        var b = a.Ka.__gm;
        a.l.bindTo("mapPixelBounds", b, "pixelBounds");
        a.l.bindTo("panningEnabled", a.Ka, "draggable");
        a.l.bindTo("panes", b)
    };
    zR = function (a) {
        var b = a.Ka.__gm;
        _.R.addListener(a.D, "dragging_changed", function () {
            b.set("markerDragging", a.j.get("dragging"))
        });
        b.set("markerDragging", b.get("markerDragging") || a.j.get("dragging"))
    };
    AR = function (a) {
        a.B.push(_.R.forward(a.l, "panbynow", a.Ka.__gm));
        _.D(HR, function (b) {
            a.B.push(_.R.addListener(a.l, b, function (c) {
                var d = a.G ? xR(a) : a.j.get("internalPosition");
                c = new _.Ak(d, c, a.l.get("position"));
                _.R.trigger(a.j, b, c)
            }))
        })
    };
    BR = function (a) {
        function b() {
            a.j.get("place") ? a.l.set("draggable", !1) : a.l.set("draggable", !!a.j.get("draggable"))
        }

        a.B.push(_.R.addListener(a.D, "draggable_changed", b));
        a.B.push(_.R.addListener(a.D, "place_changed", b));
        b()
    };
    CR = function (a) {
        a.B.push(_.R.addListener(a.Ka, "projection_changed", function () {
            return IR(a)
        }));
        a.B.push(_.R.addListener(a.D, "position_changed", function () {
            return IR(a)
        }));
        a.B.push(_.R.addListener(a.D, "place_changed", function () {
            return IR(a)
        }))
    };
    DR = function (a) {
        a.B.push(_.R.addListener(a.l, "dragging_changed", function () {
            if (a.l.get("dragging")) a.ia = _.Pv(a.m), a.ia && _.Qv(a.m, a.ia); else {
                a.ia = null;
                a.K = null;
                var b = a.m.getPosition();
                if (b && (b = _.nl(b, a.Ka.get("projection")), b = JR(a, b))) {
                    var c = _.ml(b, a.Ka.get("projection"));
                    a.j.get("place") || (a.I = !1, a.j.set("position", b), a.I = !0);
                    a.m.setPosition(c)
                }
            }
        }));
        a.B.push(_.R.addListener(a.l, "deltaclientposition_changed", function () {
            var b = a.l.get("deltaClientPosition");
            if (b && (a.ia || a.K)) {
                var c = a.K || a.ia;
                a.K = {
                    clientX: c.clientX +
                        b.clientX, clientY: c.clientY + b.clientY
                };
                b = a.da.Cb(a.K);
                b = _.nl(b, a.Ka.get("projection"));
                c = a.K;
                var d = JR(a, b);
                d && (a.j.get("place") || (a.I = !1, a.j.set("position", d), a.I = !0), d.equals(b) || (b = _.ml(d, a.Ka.get("projection")), c = _.Pv(a.m, b)));
                c && _.Qv(a.m, c)
            }
        }))
    };
    ER = function (a) {
        if (a.ca) {
            a.l.bindTo("scale", a.ca);
            a.l.bindTo("position", a.ca, "pixelPosition");
            var b = a.Ka.__gm;
            a.ca.bindTo("latLngPosition", a.j, "internalPosition");
            a.ca.bindTo("focus", a.Ka, "position");
            a.ca.bindTo("zoom", b);
            a.ca.bindTo("offset", b);
            a.ca.bindTo("center", b, "projectionCenterQ");
            a.ca.bindTo("projection", a.Ka)
        }
    };
    FR = function (a) {
        if (a.ca) {
            var b = new hR(a.Ka instanceof _.$d);
            b.bindTo("internalPosition", a.ca, "latLngPosition");
            b.bindTo("place", a.j);
            b.bindTo("position", a.j);
            b.bindTo("draggable", a.j);
            a.l.bindTo("draggable", b, "actuallyDraggable")
        }
    };
    IR = function (a) {
        if (a.I) {
            var b = xR(a);
            b && a.m.setPosition(_.ml(b, a.Ka.get("projection")))
        }
    };
    JR = function (a, b) {
        var c = a.Ka.__gm.get("snappingCallback");
        return c && (a = c({latLng: b, overlay: a.j})) ? a : b
    };
    xR = function (a) {
        var b = a.j.get("place");
        a = a.j.get("position");
        return b && b.location || a
    };
    LR = function (a, b, c) {
        b instanceof _.ce ? b.__gm.j.then(function (d) {
            KR(a, b, c, d.va)
        }) : KR(a, b, c, null)
    };
    KR = function (a, b, c, d) {
        function e(e) {
            var f = b instanceof _.ce, h = f ? e.__gm.bc.map : e.__gm.bc.streetView, k = h && h.Ka == b,
                m = k != a.contains(e);
            h && m && (f ? (e.__gm.bc.map.dispose(), e.__gm.bc.map = null) : (e.__gm.bc.streetView.dispose(), e.__gm.bc.streetView = null));
            !a.contains(e) || !f && e.get("mapOnly") || k || (b instanceof _.ce ? e.__gm.bc.map = new GR(e, b, c, _.iC(b.__gm, e), d) : e.__gm.bc.streetView = new GR(e, b, c, _.vb, null))
        }

        _.R.addListener(a, "insert", e);
        _.R.addListener(a, "remove", e);
        a.forEach(e)
    };
    MR = function (a, b, c, d) {
        this.m = a;
        this.A = b;
        this.C = c;
        this.l = d
    };
    OR = function (a) {
        if (!a.j) {
            var b = a.m, c = b.ownerDocument.createElement("canvas");
            _.Pk(c);
            c.style.position = "absolute";
            c.style.top = c.style.left = "0";
            var d = c.getContext("2d"), e = NR(d), f = a.l.size;
            c.width = Math.ceil(f.J * e);
            c.height = Math.ceil(f.L * e);
            c.style.width = _.W(f.J);
            c.style.height = _.W(f.L);
            b.appendChild(c);
            a.j = c.context = d
        }
        return a.j
    };
    NR = function (a) {
        return _.Fk() / (a.webkitBackingStorePixelRatio || a.mozBackingStorePixelRatio || a.msBackingStorePixelRatio || a.oBackingStorePixelRatio || a.backingStorePixelRatio || 1)
    };
    PR = function (a, b, c) {
        a = a.C;
        a.width = b;
        a.height = c;
        return a
    };
    RR = function (a) {
        var b = QR(a), c = OR(a), d = NR(c);
        a = a.l.size;
        c.clearRect(0, 0, Math.ceil(a.J * d), Math.ceil(a.L * d));
        b.forEach(function (a) {
            c.globalAlpha = _.Bc(a.opacity, 1);
            c.drawImage(a.image, a.ld, a.md, a.Qd, a.Pd, Math.round(a.dx * d), Math.round(a.dy * d), a.Kb * d, a.Jb * d)
        })
    };
    QR = function (a) {
        var b = [];
        a.A.forEach(function (a) {
            b.push(a)
        });
        b.sort(function (a, b) {
            return a.zIndex - b.zIndex
        });
        return b
    };
    SR = function () {
        this.j = _.sv().Ba
    };
    VR = function (a, b, c) {
        var d = this;
        this.B = b;
        this.j = c;
        this.V = {};
        this.l = {};
        this.A = 0;
        this.m = !0;
        var e = {
            animating: 1,
            animation: 1,
            attribution: 1,
            clickable: 1,
            cursor: 1,
            draggable: 1,
            flat: 1,
            icon: 1,
            label: 1,
            opacity: 1,
            optimized: 1,
            place: 1,
            position: 1,
            shape: 1,
            title: 1,
            visible: 1,
            zIndex: 1
        };
        this.C = function (a) {
            a in e && (delete this.changed, d.l[_.Dd(this)] = this, TR(d))
        };
        a.j = function (a) {
            UR(d, a)
        };
        a.onRemove = function (a) {
            delete a.changed;
            delete d.l[_.Dd(a)];
            d.B.remove(a);
            d.j.remove(a);
            _.Qm("Om", "-p", a);
            _.Qm("Om", "-v", a);
            _.Qm("Smp",
                "-p", a);
            _.R.removeListener(d.V[_.Dd(a)]);
            delete d.V[_.Dd(a)]
        };
        a = a.l;
        for (var f in a) UR(this, a[f])
    };
    UR = function (a, b) {
        a.l[_.Dd(b)] = b;
        TR(a)
    };
    TR = function (a) {
        a.A || (a.A = _.xk(function () {
            a.A = 0;
            var b = a.l;
            a.l = {};
            var c = a.m, d;
            for (d in b) WR(a, b[d]);
            c && !a.m && a.j.forEach(function (b) {
                WR(a, b)
            })
        }))
    };
    WR = function (a, b) {
        var c = XR(b);
        b.changed = a.C;
        if (!b.get("animating")) if (a.B.remove(b), c && 0 != b.get("visible")) {
            a.m && 256 <= a.j.m && (a.m = !1);
            var d = b.get("optimized"), e = b.get("draggable"), f = !!b.get("animation"), g = b.get("icon");
            g = !!g && null != g.path;
            var h = null != b.get("label");
            0 == d || e || f || g || h || !d && a.m ? _.Td(a.j, b) : (a.j.remove(b), _.Td(a.B, b));
            !b.get("pegmanMarker") && (d = b.get("map"), _.Nm(d, "Om"), _.Pm("Om", "-p", b), d.getBounds() && d.getBounds().contains(c) && _.Pm("Om", "-v", b), a.V[_.Dd(b)] = a.V[_.Dd(b)] || _.R.addListener(b,
                "click", function (a) {
                    _.Pm("Om", "-i", a)
                }), a = b.get("place")) && (a.placeId ? _.Nm(d, "Smpi") : _.Nm(d, "Smpq"), _.Pm("Smp", "-p", b), b.get("attribution") && _.Nm(d, "Sma"))
        } else a.j.remove(b)
    };
    XR = function (a) {
        var b = a.get("place");
        b = b ? b.location : a.get("position");
        a.set("internalPosition", b);
        return b
    };
    YR = function (a, b, c, d) {
        this.A = c;
        this.B = new _.fC(a, d, c);
        this.j = b
    };
    $R = function (a, b, c, d) {
        var e = b.qa, f = a.A.get();
        if (!f) return null;
        f = f.fa.size;
        c = _.gC(a.B, e, new _.N(c, d));
        if (!c) return null;
        a = new _.N(c.Rc.O * f.J, c.Rc.P * f.L);
        var g = [];
        c.Ca.ta.forEach(function (a) {
            g.push(a)
        });
        g.sort(function (a, b) {
            return b.zIndex - a.zIndex
        });
        c = null;
        for (e = 0; d = g[e]; ++e) if (f = d.Gd, 0 != f.clickable && (f = f.Ub, ZR(a.x, a.y, d))) {
            c = f;
            break
        }
        c && (b.j = d);
        return c
    };
    ZR = function (a, b, c) {
        if (c.dx > a || c.dy > b || c.dx + c.Kb < a || c.dy + c.Jb < b) a = !1; else a:{
            var d = c.Gd.shape;
            a -= c.dx;
            b -= c.dy;
            c = d.coords;
            switch (d.type.toLowerCase()) {
                case "rect":
                    a = c[0] <= a && a <= c[2] && c[1] <= b && b <= c[3];
                    break a;
                case "circle":
                    d = c[2];
                    a -= c[0];
                    b -= c[1];
                    a = a * a + b * b <= d * d;
                    break a;
                default:
                    d = c.length, c[0] == c[d - 2] && c[1] == c[d - 1] || c.push(c[0], c[1]), a = 0 != _.nC(a, b, c)
            }
        }
        return a
    };
    bS = function (a, b, c) {
        this.m = b;
        var d = this;
        a.j = function (a) {
            aS(d, a, !0)
        };
        a.onRemove = function (a) {
            aS(d, a, !1)
        };
        this.l = null;
        this.j = !1;
        this.B = 0;
        this.C = c;
        a.m ? (this.j = !0, this.A()) : _.Fb(_.Zj(_.R.trigger, c, "load"))
    };
    aS = function (a, b, c) {
        4 > a.B++ ? c ? a.m.B(b) : a.m.D(b) : a.j = !0;
        a.l || (a.l = _.xk((0, _.z)(a.A, a)))
    };
    eS = function (a, b, c, d, e, f, g) {
        _.ih.call(this);
        var h = this;
        this.aa = a;
        this.B = d;
        this.m = c;
        this.l = e;
        this.A = f;
        this.j = g || _.Zi;
        b.j = function (a) {
            var b = _.ll(h.get("projection")), c = a.j;
            -64 > c.dx || -64 > c.dy || 64 < c.dx + c.Kb || 64 < c.dy + c.Jb ? (_.Td(h.m, a), c = h.l.search(_.yi)) : (c = a.latLng, c = new _.N(c.lat(), c.lng()), a.qa = c, _.sH(h.A, {
                qa: c,
                ye: a
            }), c = _.mC(h.l, c));
            for (var d = 0, e = c.length; d < e; ++d) {
                var f = c[d], g = f.Ca || null;
                if (f = cS(h, g, f.ni || null, a, b)) a.ta[_.Dd(f)] = f, _.Td(g.ta, f)
            }
        };
        b.onRemove = function (a) {
            dS(h, a)
        }
    };
    fS = function (a, b) {
        a.aa[_.Dd(b)] = b;
        var c = {O: b.ga.x, P: b.ga.y, X: b.zoom}, d = _.ll(a.get("projection")), e = _.Mj(a.j, c);
        e = new _.N(e.M, e.N);
        var f = _.Oj(a.j, c, 64 / a.j.size.J);
        c = f.min;
        f = f.max;
        c = _.ed(c.M, c.N, f.M, f.N);
        _.uH(c, d, e, function (c, e) {
            c.ni = e;
            c.Ca = b;
            b.Fb[_.Dd(c)] = c;
            _.kC(a.l, c);
            e = _.Ac(a.A.search(c), function (a) {
                return a.ye
            });
            a.m.forEach((0, _.z)(e.push, e));
            for (var f = 0, g = e.length; f < g; ++f) {
                var h = e[f], q = cS(a, b, c.ni, h, d);
                q && (h.ta[_.Dd(q)] = q, _.Td(b.ta, q))
            }
        });
        b.ba && b.ta && a.B(b.ba, b.ta)
    };
    gS = function (a, b) {
        b && (delete a.aa[_.Dd(b)], b.ta.forEach(function (a) {
            b.ta.remove(a);
            delete a.Gd.ta[_.Dd(a)]
        }), _.vc(b.Fb, function (b, d) {
            a.l.remove(d)
        }))
    };
    dS = function (a, b) {
        a.m.contains(b) ? a.m.remove(b) : a.A.remove({qa: b.qa, ye: b});
        _.vc(b.ta, function (a, d) {
            delete b.ta[a];
            d.Ca.ta.remove(d)
        })
    };
    cS = function (a, b, c, d, e) {
        if (!e) return null;
        var f = e.fromLatLngToPoint(c);
        c = e.fromLatLngToPoint(d.latLng);
        e = a.j.size;
        a = _.Gu(a.j, new _.Yc(c.x, c.y), new _.Yc(f.x, f.y), b.zoom);
        c.x = a.O * e.J;
        c.y = a.P * e.L;
        a = d.zIndex;
        _.L(a) || (a = c.y);
        a = Math.round(1E3 * a) + _.Dd(d) % 1E3;
        f = d.j;
        b = {
            image: f.image,
            ld: f.ld,
            md: f.md,
            Qd: f.Qd,
            Pd: f.Pd,
            dx: f.dx + c.x,
            dy: f.dy + c.y,
            Kb: f.Kb,
            Jb: f.Jb,
            zIndex: a,
            opacity: d.opacity,
            Ca: b,
            Gd: d
        };
        return b.dx > e.J || b.dy > e.L || 0 > b.dx + b.Kb || 0 > b.dy + b.Jb ? null : b
    };
    jS = function (a, b, c, d, e) {
        var f = hS, g = this;
        a.j = function (a) {
            iS(g, a)
        };
        a.onRemove = function (a) {
            g.l.remove(a.__gm.oe);
            delete a.__gm.oe
        };
        this.l = b;
        this.j = c;
        this.B = f;
        this.A = d;
        this.m = e
    };
    iS = function (a, b) {
        var c = b.get("internalPosition"), d = b.get("zIndex"), e = b.get("opacity"),
            f = b.__gm.oe = {Ub: b, latLng: c, zIndex: d, opacity: e, ta: {}};
        c = b.get("useDefaults");
        d = b.get("icon");
        var g = b.get("shape");
        g || d && !c || (g = a.j.shape);
        var h = d ? a.B(d) : a.j.icon, k = IQ(function () {
            if (f == b.__gm.oe && (f.j || f.l)) {
                var c = g;
                if (f.j) {
                    var d = h.size;
                    var e = b.get("anchorPoint");
                    if (!e || e.j) e = new _.N(f.j.dx + d.width / 2, f.j.dy), e.j = !0, b.set("anchorPoint", e)
                } else d = f.l.size;
                c ? c.coords = c.coords || c.coord : c = {
                    type: "rect", coords: [0, 0, d.width,
                        d.height]
                };
                f.shape = c;
                f.clickable = b.get("clickable");
                f.title = b.get("title") || null;
                f.cursor = b.get("cursor") || "pointer";
                _.Td(a.l, f)
            }
        });
        h.url ? a.A.load(h, function (a) {
            f.j = a;
            k()
        }) : (f.l = a.m(h), k())
    };
    hS = function (a) {
        if (_.Ec(a)) {
            var b = hS.j;
            return b[a] = b[a] || {url: a}
        }
        return a
    };
    kS = function (a, b, c) {
        var d = new _.Sd, e = new _.Sd, f = new SR;
        new jS(a, d, new aR, f, c);
        var g = _.Ik(b.getDiv()).createElement("canvas"), h = {};
        a = _.ed(-100, -300, 100, 300);
        var k = new _.jC(a, void 0);
        a = _.ed(-90, -180, 90, 180);
        var m = _.tH(a, function (a, b) {
            return a.ye == b.ye
        }), p = null, q = null, t = new _.Yd(null, void 0), w = b.__gm;
        w.j.then(function (a) {
            w.m.register(new YR(h, w, t, a.va.l));
            a.Nc.ja(function (a) {
                if (a && p != a.fa) {
                    q && q.unbindAll();
                    var c = p = a.fa;
                    q = new eS(h, d, e, function (a, b) {
                        return new bS(b, new MR(a, b, g, c), a)
                    }, k, m, p);
                    q.bindTo("projection",
                        b);
                    t.set(q.Na())
                }
            })
        });
        _.hC(b, t, "markerLayer", -1)
    };
    lS = _.l();
    _.N.prototype.Jf = _.ej(5, function () {
        return Math.sqrt(this.x * this.x + this.y * this.y)
    });
    _.A(KQ, _.S);
    KQ.prototype.position_changed = function () {
        this.j || (this.j = !0, this.set("rawPosition", this.get("position")), this.j = !1)
    };
    KQ.prototype.rawPosition_changed = function () {
        this.j || (this.j = !0, this.set("position", LQ(this, this.get("rawPosition"))), this.j = !1)
    };
    var $Q = {
        linear: _.na(), "ease-out": function (a) {
            return 1 - Math.pow(a - 1, 2)
        }, "ease-in": function (a) {
            return Math.pow(a, 2)
        }
    }, OQ;
    QQ.prototype.start = function () {
        this.j.Xb = this.j.Xb || 1;
        this.j.duration = this.j.duration || 1;
        _.R.addDomListenerOnce(this.sa, "webkitAnimationEnd", (0, _.z)(function () {
            this.l = !0;
            _.R.trigger(this, "done")
        }, this));
        TQ(this.sa, PQ(this.m), this.j)
    };
    QQ.prototype.cancel = function () {
        TQ(this.sa, null, {});
        _.R.trigger(this, "done")
    };
    QQ.prototype.stop = function () {
        this.l || _.R.addDomListenerOnce(this.sa, "webkitAnimationIteration", (0, _.z)(this.cancel, this))
    };
    var WQ = null, UQ = [];
    RQ.prototype.start = function () {
        UQ.push(this);
        WQ || (WQ = window.setInterval(XQ, 10));
        this.m = _.vk();
        VQ(this)
    };
    RQ.prototype.cancel = function () {
        this.j || (this.j = !0, ZQ(this, 1), _.R.trigger(this, "done"))
    };
    RQ.prototype.stop = function () {
        this.j || (this.l = 1)
    };
    var wR = {};
    wR[1] = {
        options: {duration: 700, Xb: "infinite"},
        icon: new window.Animation([{time: 0, translate: [0, 0], ib: "ease-out"}, {
            time: .5,
            translate: [0, -20],
            ib: "ease-in"
        }, {time: 1, translate: [0, 0], ib: "ease-out"}])
    };
    wR[2] = {
        options: {duration: 500, Xb: 1},
        icon: new window.Animation([{time: 0, translate: [0, -500], ib: "ease-in"}, {
            time: .5,
            translate: [0, 0],
            ib: "ease-out"
        }, {time: .75, translate: [0, -20], ib: "ease-in"}, {time: 1, translate: [0, 0], ib: "ease-out"}])
    };
    wR[3] = {
        options: {duration: 200, Jf: 20, Xb: 1, ti: !1},
        icon: new window.Animation([{time: 0, translate: [0, 0], ib: "ease-in"}, {
            time: 1,
            translate: [0, -20],
            ib: "ease-out"
        }])
    };
    wR[4] = {
        options: {duration: 500, Jf: 20, Xb: 1, ti: !1},
        icon: new window.Animation([{time: 0, translate: [0, -20], ib: "ease-in"}, {
            time: .5,
            translate: [0, 0],
            ib: "ease-out"
        }, {time: .75, translate: [0, -10], ib: "ease-in"}, {time: 1, translate: [0, 0], ib: "ease-out"}])
    };
    var cR;
    _.A(dR, _.S);
    dR.prototype.changed = function (a) {
        "modelIcon" != a && "modelShape" != a && "modelCross" != a && "modelLabel" != a || _.hg(this.T)
    };
    _.A(gR, _.S);
    gR.prototype.changed = function () {
        if (!this.l) {
            var a = fR(this);
            this.j != a && (this.j = a, this.l = !0, this.set("shouldRender", this.j), this.l = !1)
        }
    };
    _.A(hR, _.S);
    hR.prototype.internalPosition_changed = function () {
        if (!this.j) {
            this.j = !0;
            var a = this.get("position"), b = this.get("internalPosition");
            a && b && !a.equals(b) && this.set("position", this.get("internalPosition"));
            this.j = !1
        }
    };
    hR.prototype.place_changed = hR.prototype.position_changed = hR.prototype.draggable_changed = function () {
        if (!this.j) {
            this.j = !0;
            if (this.l) {
                var a = this.get("place");
                a ? this.set("internalPosition", a.location) : this.set("internalPosition", this.get("position"))
            }
            this.get("place") ? this.set("actuallyDraggable", !1) : this.set("actuallyDraggable", this.get("draggable"));
            this.j = !1
        }
    };
    _.n = iR.prototype;
    _.n.setOpacity = function (a) {
        this.B = a;
        _.hg(this.j)
    };
    _.n.setLabel = function (a) {
        this.A = a;
        _.hg(this.j)
    };
    _.n.setVisible = function (a) {
        this.C = a;
        _.hg(this.j)
    };
    _.n.setZIndex = function (a) {
        this.D = a;
        _.hg(this.j)
    };
    _.n.release = function () {
        this.m = null;
        kR(this)
    };
    _.n.Qi = function () {
        if (this.m && this.A && 0 != this.C) {
            var a = this.m.markerLayer, b = this.A;
            this.l ? a.appendChild(this.l) : this.l = _.X("div", a);
            a = this.l;
            this.pa && _.Nk(a, this.pa);
            var c = a.firstChild;
            c || (c = _.X("div", a), c.style.height = "100px", c.style.marginTop = "-50px", c.style.marginLeft = "-50%", c.style.display = "table", c.style.borderSpacing = "0");
            var d = c.firstChild;
            d || (d = _.X("div", c), d.style.display = "table-cell", d.style.verticalAlign = "middle", d.style.whiteSpace = "nowrap", d.style.textAlign = "center");
            c = d.firstChild || _.X("div",
                d);
            _.Kk(c, b.text);
            c.style.color = b.color;
            c.style.fontSize = b.fontSize;
            c.style.fontWeight = b.fontWeight;
            c.style.fontFamily = b.fontFamily;
            _.Ev(c, _.Bc(this.B, 1));
            _.Ok(a, this.D)
        } else kR(this)
    };
    var vR = (0, _.z)(function (a, b, c) {
        _.Kk(b, "");
        var d = _.Fk(), e = _.Ik(b).createElement("canvas");
        e.width = c.size.width * d;
        e.height = c.size.height * d;
        e.style.width = _.W(c.size.width);
        e.style.height = _.W(c.size.height);
        _.ne(b, c.size);
        b.appendChild(e);
        _.Nk(e, _.vi);
        _.Pk(e);
        b = e.getContext("2d");
        b.lineCap = b.lineJoin = "round";
        b.scale(d, d);
        a = a(b);
        b.beginPath();
        _.xC(a, c.j, c.anchor.x, c.anchor.y, c.rotation || 0, c.scale);
        c.fillOpacity && (b.fillStyle = c.fillColor, b.globalAlpha = c.fillOpacity, b.fill());
        c.strokeWeight && (b.lineWidth =
            c.strokeWeight, b.strokeStyle = c.strokeColor, b.globalAlpha = c.strokeOpacity, b.stroke())
    }, null, function (a) {
        return new _.wC(a)
    });
    _.A(tR, _.S);
    _.n = tR.prototype;
    _.n.panes_changed = function () {
        lR(this);
        _.hg(this.T)
    };
    _.n.gd = function (a) {
        this.set("position", a && new _.N(a.J, a.L))
    };
    _.n.cd = function () {
        this.unbindAll();
        this.set("panes", null);
        this.l && this.l.stop();
        this.K && (_.R.removeListener(this.K), this.K = null);
        this.l = null;
        uR(this.Gc);
        this.Gc = [];
        lR(this);
        oR(this)
    };
    _.n.hg = function () {
        var a;
        if (!(a = this.td != (0 != this.get("clickable")) || this.ud != this.getDraggable())) {
            a = this.Ic;
            var b = this.get("shape");
            if (null == a || null == b) a = a == b; else {
                var c;
                if (c = a.type == b.type) a:if (a = a.coords, b = b.coords, _.Oa(a) && _.Oa(b) && a.length == b.length) {
                    c = a.length;
                    for (var d = 0; d < c; d++) if (a[d] !== b[d]) {
                        c = !1;
                        break a
                    }
                    c = !0
                } else c = !1;
                a = c
            }
            a = !a
        }
        a && (this.td = 0 != this.get("clickable"), this.ud = this.getDraggable(), this.Ic = this.get("shape"), oR(this), _.hg(this.T))
    };
    _.n.shape_changed = tR.prototype.hg;
    _.n.clickable_changed = tR.prototype.hg;
    _.n.draggable_changed = tR.prototype.hg;
    _.n.qb = function () {
        _.hg(this.T)
    };
    _.n.cursor_changed = tR.prototype.qb;
    _.n.scale_changed = tR.prototype.qb;
    _.n.raiseOnDrag_changed = tR.prototype.qb;
    _.n.crossOnDrag_changed = tR.prototype.qb;
    _.n.zIndex_changed = tR.prototype.qb;
    _.n.opacity_changed = tR.prototype.qb;
    _.n.title_changed = tR.prototype.qb;
    _.n.cross_changed = tR.prototype.qb;
    _.n.icon_changed = tR.prototype.qb;
    _.n.visible_changed = tR.prototype.qb;
    _.n.dragging_changed = tR.prototype.qb;
    _.n.position_changed = function () {
        this.Rb ? this.T.Ma() : _.hg(this.T)
    };
    _.n.getPosition = _.Od("position");
    _.n.getPanes = _.Od("panes");
    _.n.Ri = _.Od("visible");
    _.n.getDraggable = function () {
        return !!this.get("draggable")
    };
    _.n.Ti = function () {
        this.set("dragging", !0);
        this.yb.set("snappingCallback", this.Ud)
    };
    _.n.Si = function () {
        this.yb.set("snappingCallback", null);
        this.set("dragging", !1)
    };
    _.n.animation_changed = function () {
        this.Tb = !1;
        this.get("animation") ? sR(this) : (this.set("animating", !1), this.l && this.l.stop())
    };
    _.n.vf = _.Od("icon");
    _.n.ck = _.Od("label");
    var HR = "click dblclick mouseup mousedown mouseover mouseout rightclick dragstart drag dragend".split(" ");
    GR.prototype.dispose = function () {
        this.l.set("animation", null);
        this.l.cd();
        this.da && this.m ? this.da.Wc(this.m) : this.l.cd();
        this.C && this.C.unbindAll();
        this.ca && this.ca.unbindAll();
        this.A.unbindAll();
        this.D.unbindAll();
        _.D(this.B, _.R.removeListener);
        this.B.length = 0
    };
    MR.prototype.B = MR.prototype.D = function (a) {
        var b = QR(this), c = OR(this), d = NR(c), e = Math.round(a.dx * d), f = Math.round(a.dy * d),
            g = Math.ceil(a.Kb * d);
        a = Math.ceil(a.Jb * d);
        var h = PR(this, g, a), k = h.getContext("2d");
        k.translate(-e, -f);
        b.forEach(function (a) {
            k.globalAlpha = _.Bc(a.opacity, 1);
            k.drawImage(a.image, a.ld, a.md, a.Qd, a.Pd, Math.round(a.dx * d), Math.round(a.dy * d), a.Kb * d, a.Jb * d)
        });
        c.clearRect(e, f, g, a);
        c.globalAlpha = 1;
        c.drawImage(h, e, f)
    };
    SR.prototype.load = function (a, b) {
        return this.j.load(new _.UA(a.url), function (c) {
            if (c) {
                var d = c.size, e = a.size || a.scaledSize || d;
                a.size = e;
                var f = a.anchor || new _.N(e.width / 2, e.height), g = {};
                g.image = c;
                c = a.scaledSize || d;
                var h = c.width / d.width, k = c.height / d.height;
                g.ld = a.origin ? a.origin.x / h : 0;
                g.md = a.origin ? a.origin.y / k : 0;
                g.dx = -f.x;
                g.dy = -f.y;
                g.ld * h + e.width > c.width ? (g.Qd = d.width - g.ld * h, g.Kb = c.width) : (g.Qd = e.width / h, g.Kb = e.width);
                g.md * k + e.height > c.height ? (g.Pd = d.height - g.md * k, g.Jb = c.height) : (g.Pd = e.height / k, g.Jb =
                    e.height);
                b(g)
            } else b(null)
        })
    };
    SR.prototype.cancel = function (a) {
        this.j.cancel(a)
    };
    YR.prototype.l = function (a) {
        return "dragstart" != a && "drag" != a && "dragend" != a
    };
    YR.prototype.m = function (a, b) {
        return b ? $R(this, a, -8, 0) || $R(this, a, 0, -8) || $R(this, a, 8, 0) || $R(this, a, 0, 8) : $R(this, a, 0, 0)
    };
    YR.prototype.handleEvent = function (a, b, c) {
        var d = b.j;
        if ("mouseout" == a) this.j.set("cursor", ""), this.j.set("title", null); else if ("mouseover" == a) {
            var e = d.Gd;
            this.j.set("cursor", e.cursor);
            (e = e.title) && this.j.set("title", e)
        }
        d = d && "mouseout" != a ? d.Gd.latLng : b.latLng;
        "dblclick" == a && _.vd(b.ya);
        _.R.trigger(c, a, new _.Ak(d))
    };
    YR.prototype.zIndex = 40;
    bS.prototype.A = function () {
        this.j && RR(this.m);
        this.j = !1;
        this.l = null;
        this.B = 0;
        _.Fb(_.Zj(_.R.trigger, this.C, "load"))
    };
    _.gj(eS, _.ih);
    eS.prototype.Na = function () {
        return {fa: this.j, cb: !0, fb: 2, Va: this.C.bind(this)}
    };
    eS.prototype.C = function (a, b) {
        var c = this;
        b = void 0 === b ? {} : b;
        var d = !1, e = window.document.createElement("div"), f = this.j.size;
        e.style.width = f.J + "px";
        e.style.height = f.L + "px";
        e.style.overflow = "hidden";
        _.R.addListenerOnce(e, "load", function () {
            d = !0;
            b.za && b.za()
        });
        f = {ba: e, zoom: a.X, ga: new _.N(a.O, a.P), Fb: {}, ta: new _.Sd};
        e.Ca = f;
        fS(this, f);
        return {
            ga: a, Aa: function () {
                return e
            }, Bb: function () {
                return d
            }, release: function () {
                var a = e.Ca;
                e.Ca = null;
                gS(c, a);
                _.Kk(e, "");
                b.Oa && b.Oa()
            }, freeze: _.l()
        }
    };
    hS.j = {};
    lS.prototype.j = function (a, b) {
        var c = _.IC();
        if (b instanceof _.$d) LR(a, b, c); else {
            var d = new _.Sd;
            LR(d, b, c);
            var e = new _.Sd;
            kS(e, b, c);
            new VR(a, e, d)
        }
        _.R.addListener(b, "idle", function () {
            a.forEach(function (a) {
                var c = a.get("internalPosition"), d = b.getBounds();
                c && !a.pegmanMarker && d && d.contains(c) ? _.Pm("Om", "-v", a) : _.Qm("Om", "-v", a)
            })
        })
    };
    _.Ie("marker", new lS);
});
