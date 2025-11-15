{{- define "my-cluster.fullname" -}}
{{ include "my-cluster.name" . }}-{{ .Chart.AppVersion }}
{{- end -}}

{{- define "my-cluster.name" -}}
{{ .Chart.Name }}
{{- end -}}
