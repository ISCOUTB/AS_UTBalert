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
                width=300,
                height=140,
                border_radius=4,
                bgcolor="#FEE2E2",  # Fondo rojo suave
                border=ft.border.all(1, "#EF4444"),
                padding=15,
                content=ft.Stack([
                    ft.Column([
                        ft.Text("RIESGO ALTO", size=14, weight=ft.FontWeight.BOLD, color="#991B1B"),
                        ft.Text("12", size=48, weight=ft.FontWeight.BOLD, color="black"),
                    ], spacing=2),
                    ft.Container(
                        bgcolor="#FF6B35",  # Naranja UTB
                        border_radius=4,
                        width=35,
                        height=35,
                        right=0,
                        bottom=0,
                        content=ft.Icon(ft.Icons.ARROW_FORWARD, color="white", size=18)
                    )
                ])
            )

            riesgo_medio = ft.Container(
                width=300,
                height=140,
                border_radius=4,
                bgcolor="#FEF3C7",  # Fondo amarillo ocre suave
                border=ft.border.all(1, "#F59E0B"),
                padding=15,
                content=ft.Stack([
                    ft.Column([
                        ft.Text("RIESGO MEDIO", size=14, weight=ft.FontWeight.BOLD, color="#92400E"),
                        ft.Text("28", size=48, weight=ft.FontWeight.BOLD, color="black"),
                    ], spacing=2),
                    ft.Container(
                        bgcolor="#FF6B35",
                        border_radius=4,
                        width=35,
                        height=35,
                        right=0,
                        bottom=0,
                        content=ft.Icon(ft.Icons.ARROW_FORWARD, color="white", size=18)
                    )
                ])
            )

            riesgo_bajo = ft.Container(
                width=300,
                height=140,
                border_radius=4,
                bgcolor="#DCFCE7",  # Fondo verde suave
                border=ft.border.all(1, "#22C55E"),
                padding=15,
                content=ft.Stack([
                    ft.Column([
                        ft.Text("RIESGO BAJO", size=14, weight=ft.FontWeight.BOLD, color="#166534"),
                        ft.Text("105", size=48, weight=ft.FontWeight.BOLD, color="black"),
                    ], spacing=2),
                    ft.Container(
                        bgcolor="#FF6B35",
                        border_radius=4,
                        width=35,
                        height=35,
                        right=0,
                        bottom=0,
                        content=ft.Icon(ft.Icons.ARROW_FORWARD, color="white", size=18)
                    )
                ])
            )

            # ---------- TABLA ----------
            tabla = ft.DataTable(
                heading_row_color="#00B5E2",  # Fondo Cyan UTB para los títulos
                columns=[
                    ft.DataColumn(ft.Text("ESTUDIANTE", color="white", weight=ft.FontWeight.BOLD)),
                    ft.DataColumn(ft.Text("PROMEDIO", color="white", weight=ft.FontWeight.BOLD)),
                    ft.DataColumn(ft.Text("ASISTENCIA", color="white", weight=ft.FontWeight.BOLD)),
                    ft.DataColumn(ft.Text("RIESGO", color="white", weight=ft.FontWeight.BOLD)),
                    ft.DataColumn(ft.Text("ACCIÓN", color="white", weight=ft.FontWeight.BOLD))
                ],
                # Las filas permanecen igual, solo puedes ajustar la propiedad 'shape' de los botones 
                # internos si deseas que sean rectangulares en lugar de ovalados.
                rows=[

                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text("Juan Pérez", color="black")),
                            ft.DataCell(ft.Text("2.1", color="black")),
                            ft.DataCell(ft.Text("55%", color="black")),
                            ft.DataCell(ft.Text("ALTO", color="black")),

                            ft.DataCell(
                                # Ejemplo para el botón de Juan Pérez
                                ft.ElevatedButton(
                                "Intervenir ➔",
                                bgcolor="#0033A0", # Azul UTB para mantener consistencia
                                color="white",
                                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=4)),
                                on_click=lambda e: mostrar_alerta("Juan Pérez", "ALTO")
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
                                "Seguimiento ➔",
                                bgcolor="#0033A0", # Azul UTB para mantener consistencia
                                color="white",
                                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=4)),
                                on_click=lambda e: mostrar_alerta("María Gómez", "MEDIO")
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
                                "Ver Detalle ➔",
                                bgcolor="#0033A0", # Azul UTB para mantener consistencia
                                color="white",
                                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=4)),
                                on_click=lambda e: mostrar_alerta("Carlos Ruiz", "BAJO")
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
                        icon=ft.Icons.DOWNLOAD,
                        bgcolor="#0033A0",
                        color="white",
                        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=4))
                    ),
                    ft.ElevatedButton(
                        "Sincronizar Banner",
                        icon=ft.Icons.REFRESH,
                        bgcolor="#0033A0",
                        color="white",
                        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=4))
                    ),
                    ft.ElevatedButton(
                        "Enviar Alertas",
                        icon=ft.Icons.NOTIFICATIONS,
                        bgcolor="#0033A0",
                        color="white",
                        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=4))
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

            # ---------- NAVBAR INSTITUCIONAL ----------
            navbar = ft.Container(
                bgcolor="#0033A0",  # Azul UTB
                padding=ft.padding.symmetric(horizontal=20, vertical=12),
                content=ft.Row(
                    controls=[
                        ft.Row([
                            ft.Icon(ft.Icons.SCHOOL, color="white", size=28),
                            ft.Text("UTB", size=35, weight=ft.FontWeight.BOLD, color="white"),
                            ft.Text(" | Alertas Tempranas", size=18, color="white"),
                        ], spacing=10),
                        ft.Row([
                            ft.Icon(ft.Icons.PERSON, color="white", size=20),
                            ft.Text("[ Coord. Académico ]", color="white", weight=ft.FontWeight.W_500),
                        ], spacing=5)
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                )
            )

            # ---------- CONTENEDOR PRINCIPAL ----------
            page.add(
                ft.Column([
                    navbar,
                    ft.Container(
                        expand=True,
                        bgcolor="#F8FAFC",  # Gris muy claro de fondo
                        alignment=ft.Alignment(0, 0),
                        padding=30,
                        content=dashboard
                    )
                ], spacing=0, expand=True)
            )

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

#hola_mundo
