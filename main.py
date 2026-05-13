import flet as ft

def main(page: ft.Page):

    # ---------------- CONFIGURACION ----------------
    page.title = "UTB ALERT"
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 1200
    page.window_height = 750
    page.bgcolor = "#0f172a"
    page.scroll = "auto"

    # ---------------- FUNCIONES ----------------

    def mostrar_alerta(nombre, riesgo):

        mensaje.value = f"⚠ Intervención recomendada para {nombre} | Riesgo {riesgo}"
        mensaje.color = "red"

        page.snack_bar = ft.SnackBar(
            ft.Text(f"Acción ejecutada sobre {nombre}")
        )

        page.snack_bar.open = True
        page.update()

    def abrir_dashboard(e):

        if usuario.value != "" and password.value != "":

            # CAMBIAR FONDO A BLANCO
            page.bgcolor = "white"

            # LIMPIAR PANTALLA
            page.controls.clear()

            # ---------- TITULO ----------
            titulo = ft.Text(
                "Alertas Tempranas",
                size=34,
                weight=ft.FontWeight.BOLD,
                color="black"
            )

            subtitulo = ft.Text(
                "Monitoreo predictivo de riesgo estudiantil",
                size=16,
                color="black"
            )

            # ---------- TARJETAS ----------
            riesgo_alto = ft.Container(
                width=250,
                height=130,
                border_radius=20,
                bgcolor="#dc2626",
                padding=20,

                content=ft.Column([
                    ft.Text(
                        "RIESGO ALTO",
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        color="white"
                    ),

                    ft.Text(
                        "12 estudiantes",
                        size=40,
                        weight=ft.FontWeight.BOLD,
                        color="white"
                    ),

                    ft.Text(
                        "Estudiantes críticos",
                        color="black"
                    )
                ])
            )

            riesgo_medio = ft.Container(
                width=250,
                height=130,
                border_radius=20,
                bgcolor="#f59e0b",
                padding=20,

                content=ft.Column([
                    ft.Text(
                        "RIESGO MEDIO",
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        color="white"
                    ),

                    ft.Text(
                        "28",
                        size=40,
                        weight=ft.FontWeight.BOLD,
                        color="white"
                    ),

                    ft.Text(
                        "Necesitan seguimiento",
                        color="white"
                    )
                ])
            )

            riesgo_bajo = ft.Container(
                width=250,
                height=130,
                border_radius=20,
                bgcolor="#16a34a",
                padding=20,

                content=ft.Column([
                    ft.Text(
                        "RIESGO BAJO",
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        color="white"
                    ),

                    ft.Text(
                        "105",
                        size=40,
                        weight=ft.FontWeight.BOLD,
                        color="white"
                    ),

                    ft.Text(
                        "Estables",
                        color="white"
                    )
                ])
            )

            # ---------- TABLA ----------
            tabla = ft.DataTable(

                columns=[
                    ft.DataColumn(ft.Text("Estudiante",color="black")),
                    ft.DataColumn(ft.Text("Promedio",color="black")),
                    ft.DataColumn(ft.Text("Asistencia",color="black")),
                    ft.DataColumn(ft.Text("Riesgo",color="black")),
                    ft.DataColumn(ft.Text("Acción",color="black"))
                ],

                rows=[

                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text("Juan Pérez", color="black")),
                            ft.DataCell(ft.Text("2.1", color="black")),
                            ft.DataCell(ft.Text("55%", color="black")),
                            ft.DataCell(ft.Text("ALTO", color="black")),

                            ft.DataCell(
                                ft.ElevatedButton(
                                    "Intervenir",
                                    bgcolor="red",
                                    color="white",
                                    on_click=lambda e:
                                    mostrar_alerta(
                                        "Juan Pérez",
                                        "ALTO"
                                    )
                                )
                            )
                        ]
                    ),

                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text("María Gómez", color="black")),
                            ft.DataCell(ft.Text("3.0", color="black")),
                            ft.DataCell(ft.Text("70%", color="black")),
                            ft.DataCell(ft.Text("MEDIO", color="black")),

                            ft.DataCell(
                                ft.ElevatedButton(
                                    "Seguimiento",
                                    bgcolor="orange",
                                    color="white",
                                    on_click=lambda e:
                                    mostrar_alerta(
                                        "María Gómez",
                                        "MEDIO"
                                    )
                                )
                            )
                        ]
                    ),

                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text("Carlos Ruiz", color="black")),
                            ft.DataCell(ft.Text("4.5",color="black")),
                            ft.DataCell(ft.Text("95%",color="black")),
                            ft.DataCell(ft.Text("BAJO",color="black")),

                            ft.DataCell(
                                ft.ElevatedButton(
                                    "Ver",
                                    bgcolor="green",
                                    color="white",
                                    on_click=lambda e:
                                    mostrar_alerta(
                                        "Carlos Ruiz",
                                        "BAJO"
                                    )
                                )
                            )
                        ]
                    )
                ]
            )

            # ---------- MENSAJE ----------
            global mensaje
            mensaje = ft.Text(size=18)

            # ---------- BOTONES ----------
            botones = ft.Row(

                controls=[

                    ft.ElevatedButton(
                        "Generar Reporte",
                        icon=ft.Icons.DOWNLOAD
                    ),

                    ft.ElevatedButton(
                        "Actualizar Datos",
                        icon=ft.Icons.REFRESH
                    ),

                    ft.ElevatedButton(
                        "Enviar Alertas",
                        icon=ft.Icons.NOTIFICATIONS
                    )
                ],

                alignment=ft.MainAxisAlignment.CENTER,
                spacing=20
            )

            # ---------- DASHBOARD ----------
            dashboard = ft.Column(

                controls=[

                    titulo,
                    subtitulo,

                    ft.Row(
                        controls=[
                            riesgo_alto,
                            riesgo_medio,
                            riesgo_bajo
                        ],
                        spacing=20,
                        alignment=ft.MainAxisAlignment.CENTER
                    ),

                    botones,

                    ft.Text(
                        "Listado Priorizado de Casos",
                        size=24,
                        weight=ft.FontWeight.BOLD,
                        color="black"
                    ),

                    tabla,

                    mensaje
                ],

                spacing=30,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )

            page.add(
                ft.Container(
                    expand=True,
                    bgcolor="white",
                    alignment=ft.Alignment(0, 0),
                    padding=30,
                    content=dashboard
                )
            )

            page.update()

        else:
            mensaje_login.value = "Completa todos los campos"
            mensaje_login.color = "red"
            page.update()

    # ---------------- LOGIN ----------------

    usuario = ft.TextField(
        label="Usuario",
        width=300,
        prefix_icon=ft.Icons.PERSON
    )

    password = ft.TextField(
        label="Contraseña",
        password=True,
        can_reveal_password=True,
        width=300,
        prefix_icon=ft.Icons.LOCK
    )

    mensaje_login = ft.Text()

    login_box = ft.Container(

        width=350,
        padding=30,
        border_radius=20,
        bgcolor="#111827",

        content=ft.Column(

            controls=[

                ft.Container(
                    width=120,
                    height=120,
                    border_radius=60,
                    clip_behavior=ft.ClipBehavior.HARD_EDGE,

                    content=ft.Image(
                        src="logou.png",
                        width=120,
                        height=120
                    )
                ),

                ft.Text(
                    "UTB ALERT",
                    size=32,
                    weight=ft.FontWeight.BOLD,
                    color="white"
                ),

                ft.Text(
                    "Sistema Inteligente de Alertas",
                    color="white"
                ),

                usuario,
                password,

                ft.ElevatedButton(
                    "Ingresar",
                    width=300,
                    height=50,
                    on_click=abrir_dashboard
                ),

                mensaje_login
            ],

            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        )
    )

    page.add(
        ft.Container(
            expand=True,
            alignment=ft.Alignment(0, 0),
            content=login_box
        )
    )

ft.app(target=main)