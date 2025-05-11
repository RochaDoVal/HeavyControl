from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import Categoria, Equipamento, Fabricante, Local, Modelo, Atividade

User = get_user_model()

# 1) Inline para mostrar Equipamentos no perfil do usuário
class EquipamentoInline(admin.TabularInline):
    model = Equipamento
    fk_name = 'colaborador'
    extra = 0
    readonly_fields = ('numero_serie', 'modelo', 'categoria', 'horimetro_atual')
    can_delete = False

@admin.register(User)
class CustomUserAdmin(BaseUserAdmin):
    inlines = [EquipamentoInline]    # adiciona o inline aqui

    list_display = ('username', 'cpf', 'is_staff')
    list_filter  = ('is_staff', 'is_superuser', 'is_active')
    search_fields = ('username', 'email', 'first_name', 'last_name','cpf')
    ordering      = ('username',)

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Informações Pessoais'), {
            'fields': ('first_name', 'last_name', 'email', 'cpf')
        }),
        (_('Permissões'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
        (_('Datas Importantes'), {
            'fields': ('last_login', 'date_joined')
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username','nome','email','cpf','password1','password2','cargo'),
        }),
    )

# 2) EquipamentoAdmin com filtro por colaborador
class EquipamentoAdmin(admin.ModelAdmin):
    list_display = ('numero_serie', 'modelo', 'categoria', 'horimetro_atual')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(colaborador=request.user)

# Registrar os modelos
admin.site.register(Categoria)
admin.site.register(Fabricante)
admin.site.register(Local)
admin.site.register(Modelo)
admin.site.register(Atividade)
admin.site.register(Equipamento, EquipamentoAdmin)  # usa o seu EquipamentoAdmin
